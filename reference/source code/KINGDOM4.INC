{//-------------------------------------------------------------------------}
{/*                                                                         }
{Copyright (C) 1987, 2009 - Apogee Software, Ltd.                           }
{                                                                           }
{This file is part of Kroz. Kroz is free software; you can redistribute it  }
{and/or modify it under the terms of the GNU General Public License         }
{as published by the Free Software Foundation; either version 2             }
{of the License, or (at your option) any later version.                     }
{                                                                           }
{This program is distributed in the hope that it will be useful,            }
{but WITHOUT ANY WARRANTY; without even the implied warranty of             }
{MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.                       }
{                                                                           }
{See the GNU General Public License for more details.                       }
{                                                                           }
{You should have received a copy of the GNU General Public License          }
{along with this program; if not, write to the Free Software                }
{Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.}
{                                                                           }
{Original Source: 1987-1990 Scott Miller                                    }
{Prepared for public release: 03/19/09 - Joe Siegler, Apogee Software, Ltd. }
{*/                                                                         }
{//-------------------------------------------------------------------------}
{*** KINGDOM OF KROZ II title stuff.  By Scott Miller 08/31/89 ***}

unit KINGDOM4;

interface

// Declaration of procedures and functions used in the game

procedure Screen;
procedure Init_Screen;
procedure Parse_Field;
procedure Create_Playfield;
procedure Display_Playfield;
function  GetKey:byte;
procedure Hit(X, Y:integer;ch:char);
procedure Secret_Message;
procedure Shoot_Right(XWay,YWay:integer; Human:boolean);
procedure Shoot_Left(XWay,YWay:integer; Human:boolean);
procedure Tome_Message;
procedure Tome_Effects;

implementation {--------------------------------------------------------------}

// Importing necessary units for the game

uses CRT, Turbo3, DOS, Kingdom1, Kingdom2, Kingdom3;

// Procedure to display the title screen and ask for user input regarding screen type and PC speed

procedure Screen;
 begin
  ClearKeys; // Clear any previous key inputs
  Color := true; // Assume color screen by default
  bak(0,0); // Set background color
  clrscr; // Clear the screen
  bor(3); // Set border color
  cur(3); // Set cursor type
  col(9,9); // Set text color
  gotoxy(31,2); // Move cursor to position
  write('KINGDOM OF KROZ II'); // Display title
  gotoxy(18,10); // Move cursor to position
  col(15,7); // Set text color
  write('Is your screen Color or Monochrome (C/M)? C'); // Ask for screen type
  gotoxy(wherex-1,wherey);cur(2); // Move cursor and set cursor type
  read(kbd,ch);sound(500);delay(30);nosound; // Read user input and play sound
  if upcase(ch)='M' then // If user selects Monochrome
   begin
    textmode(BW80); // Set text mode to black and white
    Color := false; // Set color flag to false
   end
  else Color := true; // Otherwise, set color flag to true
  bak(0,0); // Reset background color
  gotoxy(18,10); // Move cursor to position
  delline; // Delete line
  gotoxy(9,17); // Move cursor to position
  textcolor(7); // Set text color
  write('If you have an older PC (like an XT model) choose "S" for Slow.'); // Display message
  gotoxy(10,19); // Move cursor to position
  write('If you have a PC AT, 80386 chip, etc., choose "F" for Fast.'); // Display message
  gotoxy(32,21); // Move cursor to position
  write('(Default = Slow)'); // Display message
  col(15,15); // Set text color
  gotoxy(28,14); // Move cursor to position
  write('Slow or Fast PC (S/F)? S'); // Ask for PC speed
  gotoxy(wherex-1,wherey); // Move cursor to position
  read(kbd,ch);sound(300);delay(30);nosound; // Read user input and play sound
  if upcase(ch) = 'F' then FastPC := true else FastPC := false; // Set FastPC flag based on user input
  clrscr; // Clear the screen
 end;

// Procedure to initialize the game screen and variables

procedure Init_Screen;
 begin
  Slow     := #142; // Set character for slow speed
  Medium   := #153; // Set character for medium speed
  Fast     := #234; // Set character for fast speed
  Restart  := false; // Initialize restart flag
  Score    := 0; // Initialize score
  Level    := 1; // Initialize level
  Whips    := 0; // Initialize whips
  Teleports:= 0; // Initialize teleports
  Keys     := 0; // Initialize keys
  WhipPower:= 2; // Initialize whip power
  case Difficulty of // Set initial values based on difficulty level
    9:begin Gems:=250;Whips:=100;Teleports:=50;Keys:=1;WhipPower:=3; end;
    8:begin Gems:=20;Whips:=10;end;
    5:Gems:=15;
    2:Gems:=10
  end;
  FloorPattern:=false; // Initialize floor pattern flag
  Replacement:= Null; // Initialize replacement variable
  Bonus      := 0; // Initialize bonus
  LavaFlow   := false; // Initialize lava flow flag
  LavaRate   := 0; // Initialize lava rate
  Evaporate  := 0; // Initialize evaporate variable
  MagicEWalls:= false; // Initialize magic walls flag
  GravOn     := false; // Initialize gravity flag
  GravRate   := 20; // Initialize gravity rate
  GravCounter:= 0; // Initialize gravity counter
  TreeRate   := -1; // Initialize tree rate
  HideRock   := false; // Initialize hide rock flag
  HideStairs := false; // Initialize hide stairs flag
  HideLevel  := false; // Initialize hide level flag
  HideCreate := false; // Initialize hide create flag
  HideOpenWall:=false; // Initialize hide open wall flag
  HideTrap   := false; // Initialize hide trap flag
  HideGems   := false; // Initialize hide gems flag
  HideMBlock := false; // Initialize hide magic block flag
  FoundSet   := []; // Initialize found set
  if Difficulty in [2,9] then FoundSet:=[0..255]; // Set found set based on difficulty
  GenNum     := 0; // Initialize generator number
  Sideways   :=false; // Initialize sideways flag
  OneMove    := false; // Initialize one move flag
  if FastPC then GenFactor := 28 // Set generation factor based on PC speed
  else           GenFactor := 17;
  if MixUp then // If mix up mode is enabled
   begin
    Gems     :=60; // Set initial gems
    Whips    :=30; // Set initial whips
    Teleports:=15; // Set initial teleports
    Keys     :=2; // Set initial keys
    FoundSet :=[0..ToTObjects]; // Set found set
   end;
  PX       := random(XSize)+XBot; // Set initial player X position
  PY       := random(YSize)+YBot; // Set initial player Y position
  if FastPC then BTime := 9  else BTime := 2; // Set BTime based on PC speed
  if FastPC then STime := 10 else STime := 3; // Set STime based on PC speed
  if FastPC then MTime := 8  else MTime := 2; // Set MTime based on PC speed
  if FastPC then FTime := 6  else FTime := 1; // Set FTime based on PC speed
  SkipTime := 0; // Initialize skip time
  for x:=1 to TMax do T[x]:=-1; // Reset timers
  T[1]     := 5; // Set timer 1
  T[2]     := 6; // Set timer 2
  T[3]     := 7; // Set timer 3
  T[8]     := 6; // Set timer 8
  if Color then // If color mode is enabled
   begin
    window(67,1,80,25); // Set window size
    bak(1,0); // Set background color
    clrscr; // Clear the screen
    window(1,1,80,25); // Reset window size
   end;
  col(14,7); // Set text color
  print(71,1,'Score'); // Print score label
  print(71,4,'Level'); // Print level label
  print(71,7,'Gems'); // Print gems label
  print(71,10,'Whips'); // Print whips label
  print(69,13,'Teleports'); // Print teleports label
  print(71,16,'Keys'); // Print keys label
  col(11,7);bak(4,0); // Set text and background color
  print(70,19,'OPTIONS'); // Print options label
  bak(1,0); // Reset background color
  gotoxy(70,20);col(15,15);write('W');col(7,7);write('hip'); // Print whip option
  gotoxy(70,21);col(15,15);write('T');col(7,7);write('eleport'); // Print teleport option
  gotoxy(70,22);col(15,15);write('P');col(7,7);write('ause'); // Print pause option
  gotoxy(70,23);col(15,15);write('Q');col(7,7);write('uit'); // Print quit option
  gotoxy(70,24);col(15,15);write('S');col(7,7);write('ave'); // Print save option
  gotoxy(70,25);col(15,15);write('R');col(7,7);write('estore'); // Print restore option
 end; { Init_Screen }

// Procedure to parse the field data from a string

procedure Parse_Field;
  var Slot,
      Counter,
      test  : integer;
      Fetch : string[4];
 begin
  Slot:=1; // Initialize slot
  Counter:=1; // Initialize counter
  repeat
   Fetch:=copy(DF[Level],Slot,3); // Copy 3 characters from the field data
   if Fetch[1] = ' ' then begin Fetch:=Fetch[2]+Fetch[3];end; // Remove leading spaces
   if Fetch[1] = ' ' then Fetch:=Fetch[2]; // Remove leading spaces
   val(Fetch,Parsed[Counter],test); // Convert string to integer
   Slot:=Slot+3; // Move to the next slot
   Counter:=Counter+1; // Increment counter
  until Counter > ToTObjects; // Repeat until all objects are parsed
 end; { Parse_Field }

// Procedure to create the playfield

procedure Create_Playfield;
  var x,y,
      Obj,
      Loop,
      XSpot,
      YSpot : integer;
 begin
  SNum:=0; MNum:=0; FNum:=0; BNum:=0; GenNum:=0; LavaFlow := false; // Initialize counters and flags
  T[9]:=-1; // Reset timer 9
  for x:=1 to 999 do // Reset monster positions
   begin
    SX[x]:=0;SY[x]:=0; // Reset monster X, Y positions
    MX[x]:=0;MY[x]:=0; // Reset monster X, Y positions
    FX[x]:=0;FY[x]:=0; // Reset monster X, Y positions
   end;
  for x:=1 to 1300 do begin BX[x]:=0;BY[x]:=0; end; // Reset block positions
  New_Gem_Color; // Set new gem color
  for x:=XBot to XTop do // Clear the playfield
   for y:=YBot to YTop do PF[x,y]:=0;
  PF[PX,PY]:=40; // Set player position
  Parse_Field; // Parse the field data
  for Obj:=1 to ToTObjects do // Loop through all objects
    if Parsed[Obj] > 0 then // If object is present
     for Loop:=1 to Parsed[Obj] do // Loop through all instances of the object
      begin
       Done:=false; // Initialize done flag
        repeat
         XSpot:=random(XSize)+XBot; // Generate random X position
         YSpot:=random(YSize)+YBot; // Generate random Y position
         if PF[XSpot,YSpot] = 0 then // If position is empty
          begin
           PF[XSpot,YSpot]:=Obj;Done:=true; // Place object and set done flag
           case obj of // Update counters based on object type
            1: begin SNum:=SNum+1;SX[SNum]:=XSpot;SY[SNum]:=YSpot;end;
            2: begin MNum:=MNum+1;MX[MNum]:=XSpot;MY[MNum]:=YSpot;end;
            3: begin FNum:=FNum+1;FX[FNum]:=XSpot;FY[FNum]:=YSpot;end;
            36:GenNum:=GenNum+1;
            38:begin BNum:=BNum+1;BX[BNum]:=XSpot;BY[BNum]:=YSpot;end;
            46:T[9]:=32000;
           end;
          end;
        until Done; // Repeat until object is placed
      end;
 end; { Create_Playfield }

 // Procedure to display the playfield
procedure Display_Playfield;
  var XLoop,
      YLoop : integer;
 begin
  // Loop through the playfield coordinates
  for XLoop:=XBot to XTop do
   for YLoop:=YBot to YTop do
    // Check if the current position should be displayed
    if ((PF[XLoop,YLoop] > 0 )or(FloorPattern)) and (not HideLevel) then
     begin
      gotoxy(XLoop,YLoop); // Move cursor to the current position
      // Determine what to display based on the value at the current position
      case PF[XLoop,YLoop] of
       {Floor}     0:begin col(CF1,CF2);bak(BF1,BF2);write(Tile);bak(0,0)end;
       {Slow}      1:begin col(12,7);write(Slow)end;
       {Medium}    2:begin col(10,7);write(Medium)end;
       {Fast}      3:begin col(9,7);write(Fast)end;
       {Block}     4:if Level <> 71 then begin col(6,7);write(Block)end;
       {Whip}      5:begin col(15,7);write(Whip)end;
       {Stairs}    6:if not HideStairs then
                      begin bak(7,7);col(16,16);write(Stairs);bak(0,0)end;
       {Chest}     7:if random(20)=0 then begin col(15,7);write(Chance)end
                     else begin col(14,7);bak(4,0);write(Chest);bak(0,0)end;
       {SlowTime}  8:if random(35)=0 then begin col(15,7);write(Chance)end
                     else begin col(11,7);write(SlowTime)end;
       {Gem}       9:if not HideGems then begin col(GemColor,7);write(Gem)end;
       {Invisible} 10:begin col(2,7);write(Invisible)end;
       {Teleport}  11:begin col(13,7);write(Teleport)end;
       {Key}       12:if random(25)=0 then begin col(15,7);write(Chance)end
                      else begin col(12,15);write(Key)end;
       {Door}      13:begin bak(5,7);col(3,0);write(Door);bak(0,0)end;
       {Wall}      14:begin col(6,7);write(Wall)end;
       {SpeedTime} 15:if random(10)=0 then begin col(15,7);write(Chance)end
                      else begin col(11,7);write(SpeedTime)end;
       {Trap}      16:if not HideTrap then begin
                       col(7,7);write(Trap);
                      end;
       {River}     17:if level=56 then begin col(12,16);bak(4,7);write(Lava);bak(0,0)end
                      else begin col(9,0);bak(1,7);write(River);bak(0,0)end;
       {Power}     18:if random(15)=0 then begin col(15,7);write(Chance)end
                      else begin col(15,7);write(Power)end;
       {Forest}    19:begin col(2,7);write(Forest);bak(0,0)end;
       {Tree}      20,252:begin col(6,0);bak(2,7);write(Tree);bak(0,0)end;
       {Bomb}      21:if random(40)=0 then begin col(15,7);write(Chance)end
                      else begin col(15,7);write(Bomb)end;
       {Lava}      22:begin col(12,16);bak(4,7);write(Lava);bak(0,0)end;
       {Pit}       23:begin col(7,7);write(Pit)end;
       {Tome}      24:begin col(31,31);bak(5,0);write(Tome);bak(0,0);end;
       {Tunnel}    25:begin col(15,7);write(Tunnel)end;
       {Freeze}    26:begin col(11,7);write(Freeze)end;
       {Nugget}    27:begin col(14,7);write(Nugget)end;
       {Quake}     28:if random(15)=0 then begin col(15,7);write(Chance)end;
       {IBlock}    29:;
       {IWall}     30:;
       {IDoor}     31:;
       {Stop}      32:;
       {Zap}       34:begin col(12,7);write(Zap)end;
       {Create}    35:if not HideCreate then begin col(15,7);write(Chance)end;
       {Generator} 36:begin col(30,31);write(Generator)end;
       {MBlock}    38:if not hideMBlock then begin col(6,7);write(MBlock)end;
       {Trap2-13}  33,37,39,67,224..231:;
       {Player}    40:begin bak(7,7);col(16,16);write(Stairs);bak(0,0)end;
       {ShowGems}  41:;
       {Tablet}    42:begin col(9,7);write(Tablet)end;
       {ZBlock}    43:begin col(6,7);write(ZBlock)end;
       {BlockSpell}44:;
       {Chance}    45:begin col(15,7);write(Chance)end;
       {Statue}    46:begin col(31,23);write(Statue)end;
       { K }       48:begin col(14,15);write('K')end;
       { R }       49:begin col(14,15);write('R')end;
       { O }       50:begin col(14,15);write('O')end;
       { Z }       51:begin col(14,15);write('Z')end;
       {OWall1,2}  52,53:begin col(6,7);write(Wall)end;
       {OWall3}    54:begin col(7,7);write(Wall)end;
       {CWall1..3} 55..57:;
       {OSpell1..3}58..60:if not HideOpenWall then 
                      begin col(11,7);write(OSpell1)end;
       {CSpell1..3}61..63:;
       {Triggers}  68..74:;
       {GBlock}    64:begin col(7,7);write(GBlock)end;
       {Rock}      65:if not HideRock then begin col(7,7);write(Rock)end;
       {EWall}     66:begin col(12,0);bak(4,7);write(EWall);bak(0,0)end;
       {WallVanish}47:if random(20)=0 then begin col(15,7);write(Chance)end
                      else begin end;
       {Rope}      75:begin col(7,7);write(Rope)end;
       {DropRope}  76..80:begin col(7,7);write(DropRope)end;
      {ShootRight} 82:begin col(7,7);write(ShootRight)end;
      {ShootLeft}  83:begin col(7,7);write(ShootLeft)end;
       {Amulet}    81:begin col(31,31);write(Amulet)end;
       {punct.}   180:begin col(15,0);bak(6,7);write('.');bak(0,0)end;
       {punct.}   181:begin col(15,0);bak(6,7);write('?');bak(0,0)end;
       {punct.}   182:begin col(15,0);bak(6,7);write('''');bak(0,0)end;
       {punct.}   183:begin col(15,0);bak(6,7);write(',');bak(0,0)end;
       {punct.}   184:begin col(15,0);bak(6,7);write(':');bak(0,0)end;
       {punct.}   195:begin col(15,0);bak(6,7);write('!');bak(0,0)end       
       {LETTERS} else begin
                       col(15,0);bak(6,7);
                       write(upcase(chr(PF[XLoop,YLoop])));bak(0,0);
                      end;
      end;
     end;
  FloorPattern:=false; // Reset floor pattern flag
 end; { Display_Playfield }

// Function to get a key press from the user
function GetKey:byte;
      procedure BadKeySound;
       begin
        sound(540);delay(40); // Play a sound
        for x:=1 to 4 do
         begin sound(100);delay(15);nosound;delay(15) end; // Play a series of sounds
        nosound; // Stop the sound
       end;
  var key:char;
 begin
  if keypressed then // If a key is pressed
   begin
    read(kbd,key); // Read the key
    if key=#27 then // If the key is ESC
     if keypressed then { key must be an extended character }
      begin
       read(kbd,key); // Read the next key
       if key in [#72,#80,#77,#75,#71,#79,#73,#81] then // If the key is an arrow key
        GetKey:=ord(key)+100 // Return the key code
       else begin BadKeySound;GetKey:=0;end; // Play a bad key sound
      end
     else GetKey:=81 // Return the key code for ESC
    else { key must be an alpha character }
     case ord(key) of
      40:if Difficulty=9 then
          begin PF[PX+1,PY]:=6;sound(2000);delay(40);nosound;GetKey:=0;end;
      41:if Difficulty=9 then
          begin Gems:=150;Whips:=99;Teleports:=99;Keys:=9;GetKey:=0;Update_Info;end;
      43:begin
          FoundSet:=[];
          Flash(13,25,'Newly found object desciptions are reset.');
         end; 
      45:begin
          FoundSet:=[0..255];
          Flash(10,25,'References to new objects will not be displayed.');
         end; 
      119,87:GetKey:=87;       { Whip     }
      116,84:GetKey:=84;       { Teleport }
      112,80:GetKey:=80;       { Pause    }
      113,81:GetKey:=81;       { Quit     }
      115,83:GetKey:=83;       { Save     }
      114,82:GetKey:=82;       { Restore  }
      117,85:GetKey:=171;      { U-NW     }
      105,73:GetKey:=172;      { I-North  }
      111,79:GetKey:=173;      { O-NE     }
      106,74:GetKey:=175;      { J-West   }
      107,75:GetKey:=177;      { K-East   }
      110,78:GetKey:=179;      { N-SW     }
      109,77:GetKey:=180;      { M-South  }
      44    :GetKey:=181       { ,-SE     }
      else begin BadKeySound;GetKey:=0;end;
     end;
   end
  else GetKey:=0; // Return 0 if no key is pressed
 end; { GetKey }

 // Procedure to handle hitting an object at coordinates (X, Y)
procedure Hit(X, Y:integer; ch:char);
  var i : integer;
      Thing : char;
 begin
  Thing := char(PF[x,y]); // Get the character at the playfield position
  bak(0,0); // Set background color
  // Display hit animation
  for i := 1 to ord(FastPC)*150 + ord(not FastPC)*45 do
   begin col(random(16),15); gotoxy(x,y); write(ch); end;
  gotoxy(x,y); // Move cursor to the hit position
  // Handle different objects based on their type
  case integer(Thing) of
   1..3: begin
          PF[x,y] := 0; write(' '); Score := Score + integer(Thing); // Clear the object and update score
          sound(400); delay(20); sound(90); // Play sound
         end;
   4,19,20,252:
         begin
          i := WhipPower; if integer(Thing) = 19 then i := 8; // Set whip power
          case integer(Thing) of
           4: Thing := Block; 19: Thing := Forest; 20,252: Thing := Tree; // Set object type
          end;
          if random(7) < i then
           begin write(' '); PF[x,y] := 0; // Clear the object
            for i := ord(FastPC)*5700 + ord(not FastPC)*3300 downto 20 do sound(random(i)); sound(90); // Play sound
           end
          else
           begin
            sound(130); delay(25); sound(90); // Play sound
            col(6,7); // Set color
            if Thing = Tree then begin col(6,0); bak(2,7); end
            else if Thing = Forest then col(2,7);
            write(Thing); // Redraw the object
            if Thing = Tree then bak(0,0);
           end;
         end;
   6:    begin col(16,16); bak(7,7); write(Stairs); bak(0,0); end; // Draw stairs
   10,15,16,18,36,48..51:
         begin
          PF[x,y] := Null; write(' '); // Clear the object
          sound(400); delay(20); sound(90); // Play sound
          if integer(Thing) = 36 then
           begin
             for i := ord(FastPC)*5700 + ord(not FastPC)*3300 downto 20 do sound(random(i)); sound(90); // Play sound
             AddScore(36); GenNum := GenNum - 1; // Update score and generator count
           end;
         end;
       5: begin col(15,7); write(Whip) end; // Draw whip
       7: begin col(14,7); bak(4,0); write(Chest); bak(0,0) end; // Draw chest
       8: begin col(11,7); write(SlowTime) end; // Draw slow time
       9: begin col(GemColor,7); write(Gem) end; // Draw gem
      11: begin col(13,7); write(Teleport) end; // Draw teleport
      12: begin col(12,15); write(Key) end; // Draw key
      13: begin col(3,0); bak(5,7); write(Door); bak(0,0) end; // Draw door
      14,52,53: begin col(6,7); write(Wall) end; // Draw wall
      54: begin col(7,7); write(Wall) end; // Draw wall
      17: begin col(9,0); bak(1,7); write(River); bak(0,0) end; // Draw river
      21: begin col(15,7); write(Bomb) end; // Draw bomb
      22: begin col(12,16); bak(4,7); write(Lava); bak(0,0) end; // Draw lava
      23: begin col(7,7); write(Pit) end; // Draw pit
      24: begin col(31,31); bak(5,0); write(Tome); bak(0,0) end; // Draw tome
      25: begin col(15,7); write(Tunnel) end; // Draw tunnel
      26: begin col(11,7); write(Freeze) end; // Draw freeze
      27: begin col(14,7); write(Nugget) end; // Draw nugget
      28..31,33,37,39,41,44,67,224..231: begin col(0,0); bak(0,0); write(' ') end; // Clear object
      32: begin PF[x,y] := Null; write(' ') end; // Clear object
      34: begin col(12,7); write(Zap) end; // Draw zap
      35: begin col(14,7); write(Create) end; // Draw create
      42: begin col(9,7); write(Tablet) end; // Draw tablet
      45: begin col(15,7); write(Chance) end; // Draw chance
      58..60: begin col(11,7); write(OSpell1) end; // Draw spell
      66: begin col(12,0); bak(4,7); write(EWall); bak(0,0) end; // Draw wall
      47,55..57,61..63,68..74: write(' '); // Clear object
      76..80: begin col(7,7); write(DropRope) end; // Draw drop rope
      75: begin col(7,7); write(Rope) end; // Draw rope
      81: begin col(31,31); write(Amulet) end; // Draw amulet
      82: begin col(7,7); write(ShootRight) end; // Draw shoot right
      83: begin col(7,7); write(ShootLeft) end; // Draw shoot left
      46: begin
          for i := ord(FastPC)*5700 + ord(not FastPC)*3300 downto 20 do
           sound(random(i)); sound(90); // Play sound
          if random(50) < WhipPower then
           begin write(' '); PF[x,y] := 0; // Clear the object
            for i := 1 to 32000 do sound(random(5000));
            for i := 18900 downto 20 do sound(random(i)); nosound; // Play sound
            Score := Score + 10; // Update score
            T[9] := -1; // Reset timer
            Update_Info; // Update info
            ClearKeys; // Clear keys
            Flash(7,25,'You''ve destroyed the Statue!  Your Gems are now safe.'); // Display message
            sound(90); // Play sound
           end
          else begin col(31,23); write(Statue) end; // Redraw statue
         end;
       65: if random(30) < WhipPower then
           begin write(' '); PF[x,y] := 0; // Clear the object
            for i := ord(FastPC)*8700 + ord(not FastPC)*5300 downto 20 do sound(random(i)); sound(90); // Play sound
            Score := Score + 100; Update_Info; // Update score and info
           end
          else
           begin
            for i := ord(FastPC)*4700 + ord(not FastPC)*2300 downto 20 do
             sound(random(i)); sound(90); // Play sound
            col(7,7);
            write(Rock); // Redraw rock
           end;
      38,43,64: begin
          if random(7) < WhipPower then
           begin write(' '); PF[x,y] := Null; // Clear the object
            for i := ord(FastPC)*5700 + ord(not FastPC)*3300 downto 20 do
             sound(random(i)); sound(90); // Play sound
            AddScore(38); // Update score
           end
          else
           begin
            sound(130); delay(25); sound(90); // Play sound
            if integer(Thing) = 64 then col(7,7) else col(6,7);
            write(Block); // Redraw block
           end;
         end;
      0: write(' ') // Clear object
   else begin
         col(15,0); bak(6,7);
         write(upcase(chr(PF[x,y]))); bak(0,0); // Draw character
        end;
  end;
 end; { Hit }

// Procedure to display a secret message
procedure Secret_Message;
 begin
  for x := 20 to 8000 do sound(x); nosound; // Play sound
  ClearKeys; // Clear keys
  Flash(4,25,'You notice a secret message carved into the old tree...'); // Display message
  Flash(14,25,'"Goodness of Heart Overcomes Adversity."'); // Display message
  Flash(7,25,'Reveal that you found this message to Scott Miller...'); // Display message
  Flash(3,25,'And receive a "MASTER KROZ CERTIFICATE" to hang on your wall!!'); // Display message
  Flash(12,25,'Only the first 100 players to report this...'); // Display message
  Flash(9,25,'Will be awarded the certificate.  Congratulations!'); // Display message
 end; { Secret_Message }

 // Procedure to shoot a spear to the right
procedure Shoot_Right(XWay,YWay:integer; Human:boolean);
 begin
  Go(XWay,YWay,Human); // Move the player in the specified direction
  x := PX; // Set the initial x position to the player's x position
  sound(x+30); // Play a sound based on the x position
  inc(x); // Increment x to start shooting to the right
  // Loop until the spear hits an obstacle or goes out of bounds
  while (x < 66) and not (PF[x,PY] in [4,6,13,14,22,25,31,36,38,42,43,46,52..54,64..66,81]) do
   begin
    // Display the spear moving to the right
    for b := 1 to 60 do
     begin
      gotoxy(x,PY);
      col(random(15+1),15);
      write(#196);
     end;
    gotoxy(x,PY);
    col(15,15);
    write(#196); // Draw the spear
    // Check if the spear hits an object that can be destroyed
    if not (PF[x,PY] in [0,17,23,28..30,32,33,37,39,41,44,47,55..57,61..63,67..75]) then
     begin
      sound(300); delay(10); // Play a sound
      if PF[x,PY] in [1..3] then PF[x,PY] := 32 else PF[x,PY] := Null; // Destroy the object
     end;
    sound(x+30); // Play a sound based on the x position
    gotoxy(x,PY);
    col(7,7);
    // Redraw the object if it is not destroyed
    case PF[x,PY] of
     17: begin col(9,0); bak(1,7); write(River); bak(0,0) end;
     23: write(Pit);
     75: write(Rope)
     else write(' ');
    end;
    inc(x); // Move the spear to the next position
   end; nosound; // Stop the sound
   // Check if the spear triggered a magic spear
   if not(82 in FoundSet) then
    begin
     FoundSet := FoundSet + [82];
     Flash(20,25,'You triggered a Magic Spear!');
    end else ClearKeys;
 end; {Shoot_Right}

// Procedure to shoot a spear to the left
procedure Shoot_Left(XWay,YWay:integer; Human:boolean);
 begin
  Go(XWay,YWay,Human); // Move the player in the specified direction
  x := PX; // Set the initial x position to the player's x position
  sound(x+30); // Play a sound based on the x position
  dec(x); // Decrement x to start shooting to the left
  // Loop until the spear hits an obstacle or goes out of bounds
  while (x > 1) and not (PF[x,PY] in [4,6,13,14,22,25,31,36,38,42,43,46,52..54,64..66,81]) do
   begin
    // Display the spear moving to the left
    for b := 1 to 60 do
     begin
      gotoxy(x,PY);
      col(random(15+1),15);
      write(#196);
     end;
    gotoxy(x,PY);
    col(15,15);
    write(#196); // Draw the spear
    // Check if the spear hits an object that can be destroyed
    if not (PF[x,PY] in [0,17,23,28..30,32,33,37,39,41,44,47,55..57,61..63,67..75]) then
     begin
      sound(300); delay(10); // Play a sound
      if PF[x,PY] in [1..3] then PF[x,PY] := 32 else PF[x,PY] := Null; // Destroy the object
     end;
    sound(x+30); // Play a sound based on the x position
    gotoxy(x,PY);
    col(7,7);
    // Redraw the object if it is not destroyed
    case PF[x,PY] of
     17: begin col(9,0); bak(1,7); write(River); bak(0,0) end;
     23: write(Pit);
     75: write(Rope)
     else write(' ');
    end;
    dec(x); // Move the spear to the next position
   end; nosound; // Stop the sound
   // Check if the spear triggered a magic spear
   if not(83 in FoundSet) then
    begin
     FoundSet := FoundSet + [83];
     Flash(20,25,'You triggered a Magic Spear!');
    end else ClearKeys;
 end; {Shoot_Left}

// Procedure to display a message when the player finds the magical amulet
procedure Tome_Message;
 begin
  Flash(6,25,' You reach out to grab the object of your long quest... '); // Display message
  Flash(19,25,' the Magical Amulet of Kroz. '); // Display message
  Flash(7,25,' Your body surges with electricity as you clutch it! '); // Display message
 end; { Tome_Message }

// Procedure to create visual and sound effects when the player finds the magical amulet
procedure Tome_Effects;
 begin
  bak(0,0); // Set background color
  // Loop to create visual and sound effects
  for b := 7 downto 0 do
   for x := XBot to XTop do
    for y := YBot to YTop do
     if PF[x,y] = Null then
      begin
       sound(x*y*(b+1)); // Play sound based on position
       gotoxy(x,y); // Move cursor to position
       col(b*2,ord(odd(b))*7+ord(not odd(b))*0); // Set color
       write(Wall); // Draw wall
      end; nosound; // Stop the sound
 end; { Tome_Effects }

BEGIN
END.