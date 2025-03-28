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
{*** KINGDOM OF KROZ II levels.  By Scott Miller 08/31/89 ***}

unit KINGDOM1;

interface

uses Turbo3, CRT, DOS;

const // Declaring constants

// This '#' follow by a number(decimal) represents the ASCII equivalent of that number.

     {0}  Null      = 0;
{X}  {4}  Block     = #178;  
{W}  {5}  Whip      = #244;  
{L}  {6}  Stairs    = #240;  
{C}  {7}  Chest     = #67;   
{S}  {8}  SlowTime  = #232;
{+}  {9}  Gem       = #4;    
{I}  {10} Invisible = #173;   
{T}  {11} Teleport  = #24;   
{K}  {12} Key       = #140; 
{D}  {13} Door      = #236;  
{#}  {14} Wall      = #219;
{F}  {15} SpeedTime = #233;
{.}  {16} Trap      = #249;  
{R}  {17} River     = #247;
{Q}  {18} Power     = #9;    
{/}  {19} Forest    = #219;
{\}  {20} Tree      = #5;
{B}  {21} Bomb      = #157;  
{V}  {22} Lava      = #178;  
{=}  {23} Pit       = #176;
{A}  {24} Tome      = #12;
{U}  {25} Tunnel    = #239;
{Z}  {26} Freeze    = #159;
{*}  {27} Nugget    = #15;
{E}  {28} Quake     = #0;
{;}  {29} IBlock    = #30;
{:}  {30} IWall     = #0;
{`}  {31} IDoor     = #0;
{-}  {32} Stop      = #0;
{@}  {33} Trap2     = #0;
{%}  {34} Zap       = #30;  
{]}  {35} Create    = #31;
{G}  {36} Generator = #6;
{)}  {37} Trap3     = #0;   
{M}  {38} MBlock    = #178; 
{(}  {39} Trap4     = #0;  
{P}  {40} Player    = #2; // SMILEY FACE 
{&}  {41} ShowGems  = #0;
{!}  {42} Tablet    = #254;
{O}  {43} ZBlock    = #178;
{H}  {44} BlockSpell= #0;
{?}  {45} Chance    = #63;
{>}  {46} Statue    = #1;
{N}  {47} WallVanish= #0;
{<}  {48}  { K }
{[}  {49}  { R }
{|}  {50}  { O }
{"}  {51}  { Z }
{4}  {52} OWall1    = #219;
{5}  {53} OWall2    = #219;
{6}  {54} OWall3    = #219; { grey }
{7}  {55} CWall1    = #0;
{8}  {56} CWall2    = #0;
{9}  {57} CWall3    = #0;
{±}  {58} OSpell1   = #127; {ALT-241} //  Plus/Minus symbol
{≥}  {59} OSpell2   = #127; {ALT-242} //  Greater than or equal to
{≤}  {60} OSpell3   = #127; {ALT-243} //  Less than or equal to
{⌠}  {61} CSpell1   = #0;   {ALT-244} //  Integral top
{⌡}  {62} CSpell2   = #0;   {ALT-245} //  Integral bottom
{÷}  {63} CSpell3   = #0;   {ALT-246} //  Division sign
{Y}  {64} GBlock    = #178;
{0}  {65} Rock      = #79;
{~}  {66} EWall     = #88;
{ }  {67} Trap5     = #0;   {represented by a $}
{æ}  {68} TBlock    = #0;   {ALT-145} //  AE lowercase symbol
{Æ}  {69} TRock     = #0;   {ALT-146} //  AE uppercase symbol
{ô}  {70} TGem      = #0;   {ALT-147} //  o with carrot
{ö}  {71} TBlind    = #0;   {ALT-148} //  o with two dots
{ò}  {72} TWhip     = #0;   {ALT-149} //  o with down accent
{û}  {73} TGold     = #0;   {ALT-150} //  u with carrot
{ù}  {74} TTree     = #0;   {ALT-151} //  u with down accent
{J}  {75} Rope      = #179; {ALT-179} //  vert line replaced with J
{┤}  {76} DropRope  = #25;  {ALT-185} //  vert line with perpendicular left
{│}  {77}{DropRope}         {ALT-186} //  vert line thicker
{┐}  {78}{DropRope}         {ALT-187} //  left to bottom right angle
{┘}  {79}{DropRope}         {ALT-188} //  left to top right angle
{╜}  {80}{DropRope}         {ALT-189} //  left to top right angle 2
{â}  {81} Amulet    = #12;  {ALT-131} //  a with carrot
{»}  {82} ShootRight= #26;  {ALT-175} //  >>
{«}  {83} ShootLeft = #27;  {ALT-174} //  <<

{α}  {224}Trap6     = #0;   {ALT-224} //  alpha (greek)
{β}  {225}Trap7     = #0;   {ALT-225} //  beta (greek)
{┌}  {226}Trap8     = #0;   {ALT-226} //  upside down L
{π}  {227}Trap9     = #0;   {ALT-227} //  pi
{∑}  {228}Trap10    = #0;   {ALT-228} //  sigma uppercase
{σ}  {229}Trap11    = #0;   {ALT-229} //  sigma lowercase
{μ}  {230}Trap12    = #0;   {ALT-230} //  mu (greek)
{τ}  {231}Trap13    = #0;   {ALT-231} //  tau (greek)

{ⁿ}  {252}Message   = #5;   {ALT-252} //  superscript n


      TotObjects    = 83;
      Bottom        = 75;  {1472 objects max. / play field }
      XBot          = 2;
      XTop          = 65;
      YBot          = 2;
      YTop          = 24;
      YSize         = 23; // Level Height
      XSize         = 64; // Level Width
      TMax          = 9;
      GMove         = false;
      PMove         = true;


type
        Field     = string[222];   { not set for the Rope }
        StrXSize  = string[XSize];
        Str80     = string[80];
        NameStr   = string[15];
        HSType    = record
                     Name        : NameStr;
                     HighScore,
                     HighLevel   : longint;
                    end;
        SaveType  = record
                     S_Level,
                     S_Score,
                     S_Gems,
                     S_Whips,
                     S_Teleports,
                     S_Keys,
                     S_WhipPower,
                     S_Difficulty,
                     S_PX, S_PY  : longint;
                     S_FoundSet  : set of 0..ToTObjects;
                     S_MixUp     : boolean;
                    end;

var
        Parsed    : array [1..ToTObjects] of integer;
        Gems,
        Whips,
        Teleports,
        Keys,
        Difficulty,
        Level,
        PXOld, PYOld,
        SkipTime,
        BTime, STime, MTime, FTime,
        XDir, YDir,
        loop,
        width,
        xl,xr,
        yl,yr,
        Replacement,
        Bonus,
        GenFactor,
        CF1, CF2, BF1, BF2,
        x,y,i,a,b : integer;
        xb, yb    : byte;
        Result    : Registers;
        MixUp,
        Done,
        Restart   : boolean;
        FoundSet  : set of 0..ToTObjects;
        I_Score,
        I_Gems,
        I_Whips,
        I_Teleports,
        I_Keys,
        I_WhipPower,
        I_Difficulty,
        I_PX, I_PY  : longint;
        I_FoundSet  : set of 1..ToTObjects;
        SaveStuff   : SaveType;
        SaveFile    : file of SaveType;
        HSList      : array [1..15] of HSType;
        HSFile      : file of HSType;
        FileName    : file;



var   DF       : array [1..Bottom] of Field;
      PF       : array [1..66,1..25] of byte; // 2d array likely used for maps
      FP       : array [1..YSize] of StrXSize;
      BX, BY   : array [1..1300] of byte;
      SX, SY,
      MX, MY,
      FX, FY   : array [1..1000] of byte;
      T        : array [1..TMax] of integer; { 1=Slow, 2=Medium, 3=Fast }
      ch,                                    { 4=SlowTime, 5=invisible  }
      Slow,                                  { 6=SpeedTime, 7=Freeze    }
      Medium,                                { 8=MBlock, 9=Statue       }
      Fast,
      Tile     : char; 
      Score    : longint;
      StrVal   : Field;
      WhipPower,
      PX, PY,
      BC, BB,
      RX, RY,
      GenNum,
      BNum,
      SNum,
      MNum,
      FNum,
      EvapoRate,
      GravRate,     { 0=fast, 2=slow }
      GravCounter,
      TreeRate,
      LavaRate,     { 10=slow, 90=fast }
      GemColor   : integer;
      FastPC,
      LavaFlow,
      HideTrap,
      HideRock,
      HideStairs,
      HideOpenWall,
      HideCreate,
      HideMBlock,
      HideLevel,
      HideGems,
      GravOn,
      Sideways,
      OneMove,
      FloorPattern,
      MagicEWalls,
      Color    : boolean;

procedure MakeFloor(TilePattern: char; A,B,C,D: byte);
procedure Flash(XPos,YPos:byte;Message:Str80);
procedure PrintNum(YPos:byte; Num:longint);
procedure Print(XPos,YPos:byte; Message:Str80);
procedure Restore_Border;
procedure ClearKeys;
procedure Cur(Num:byte);
procedure Sign_Off;
procedure Col(Num1,Num2:byte);
procedure Bak(Num1,Num2:byte);
procedure Update_Info;
procedure Bor(Num:byte);
procedure Shareware(Wait: boolean);
procedure New_Gem_Color;
procedure Define_Levels;
procedure Won;
procedure FootStep;
procedure GrabSound;
procedure NoneSound;
procedure BlockSound;
procedure Static;
procedure End_Routine;
procedure Convert_Format;
procedure Trigger_Trap(Place:boolean; i:integer; ch:char);
procedure Go(var XWay,YWay:integer; Human:boolean);
procedure MoveRock(var XWay,YWay:integer);
procedure Dead(DeadDot: boolean);
procedure High_Score(PlayAgain:boolean);
procedure AddScore(What:integer);
procedure Play(Start,Stop,Speed:integer);
procedure Border;

implementation { ---------------------------------------------------------- }

procedure MakeFloor(TilePattern: char; A,B,C,D: byte);
 begin
  Tile := TilePattern;
  CF1  := A;
  CF2  := B;
  BF1  := C;
  BF2  := D;
  FloorPattern := True;
 end; { MakeFloor }


procedure Print(XPos,YPos:byte; Message:Str80);
 begin
  gotoxy(XPos,YPos);
  write(Message);
 end;

procedure PrintNum(YPos:byte; Num:longint);
  var TempStr : Field;
 begin
  gotoxy(70,YPos);
  write('       ');
  str(Num,StrVal);
  if (YPos=2) and (Score>0) then StrVal:=StrVal+'0';
  if (YPos=11) then 
    case WhipPower of
     0..2:;
     3..9:begin
           str(WhipPower-2,TempStr);
           StrVal:=StrVal+'+'+TempStr;
          end;  
    end; 
  gotoxy(73-length(StrVal) div 2,YPos);
  write(StrVal);
 end;
 
procedure Update_Info;
 begin
  bak(7,0);col(4,7);
  printnum(2,Score);
  printnum(5,Level);
  if Gems > 9 then printnum(8,Gems)
  else begin col(20,23);printnum(8,Gems);col(4,7);end;
  printnum(11,Whips);
  printnum(14,Teleports);
  printnum(17,Keys);
  bak(0,0);
 end; { Update_Info }

procedure Border;
 begin
  gotoxy(1,24);
  BC:=random(8)+8;
  BB:=random(7)+1;
  col(BC,0);bak(BB,7);
  for i:=1 to 66 do
   begin
    gotoxy(i,25);
    write(Block);
    gotoxy(i,1);
    write(Block);
   end;
  for i:=2 to 24 do
   begin
    gotoxy(1,i);
    write(Block);
    gotoxy(66,i);
    write(Block);
   end;
  bak(0,0);
  end; { Border }

procedure Restore_Border;
 begin    { Restores the bottom line of the border }
  gotoxy(2,25);
  col(BC,0);bak(BB,7);
  for x:=1 to 64 do write(#178);
  bak(0,0);
 end; { Restore_Border }

procedure Flash(XPos,YPos:byte;Message:Str80);
 var Counter : integer;
 begin
  Counter := 14;
  ClearKeys;
  repeat
   Counter := Counter + 1;
   if Counter > 15 then Counter := 13;
   col(Counter,15);
   delay(20);
   print(XPos,YPos,Message);
  until keypressed;
  Restore_Border;
 end;

procedure ClearKeys;
 begin
  while keypressed do read(kbd,ch);
 end;

procedure Cur(Num:byte);
 var Result : Registers;
 begin
  Result.AX := $100;
  with Result do
   if Color then
    case Num of
     1:CX:=$707;   { Underline   }
     2:CX:=$8;     { Solid Block }
     3:CX:=$2000;  { Invisible   }
    end
   else
    case Num of
     1:CX:=$C0D;
     2:CX:=$E;
     3:CX:=$2000;
    end;
   intr($10,Result);
 end; { Cur }

procedure FootStep;
  var x:integer;
 begin
  for x:=1 to ord(FastPC)*50+ord(not FastPC)*23 do sound(random(550)+350);
  nosound;delay(120);
  for x:=1 to ord(FastPC)*60+ord(not FastPC)*30 do sound(random(50)+150);
  nosound;
 end;

procedure GrabSound;
  var x:integer;
 begin
  for x:=1 to ord(FastPC)*160+ord(not FastPC)*65 do
   sound(random(1000)+1000);nosound
 end;

procedure BlockSound;
  var x:integer;
 begin
  for x:= 60 downto 30 do begin sound(x);delay(1+ord(FastPC)*2);end;
  nosound;
 end;

procedure NoneSound;
  var x:integer;
 begin
  for x:=1 to 5 do
   begin
    sound(400);delay(10);nosound;delay(10);
    sound(700);delay(10);nosound;delay(10);
   end;
 end;

procedure Static;
  var x,y:integer;
 begin for x:= 1 to 15 do bor(random(16));bor(4);
  for x:=1 to 33 do
   case random(2) of
    0:for y:=1 to random(60)+10 do sound(random(4000)+3000);
    1:begin nosound;delay(random(30)); end;
   end; nosound;
 end; { Static }
 
procedure Col(Num1,Num2:byte);
 begin if Color then textcolor(Num1) else textcolor(Num2) end;

procedure Bak(Num1,Num2:byte);
 begin if Color then textbackground(Num1) else textbackground(Num2) end;

procedure Bor(Num:byte);
 var Result : Registers;
 begin
  if Color then
    begin
      with Result do begin AX:=$B00;BX:=Num; end;
      intr($10,Result);
    end;
 end;

procedure Sign_Off; 
 begin
  Shareware(false);
  ClearKeys;
  col(7,7);
  bor(0);
  bak(0,0);
  clrscr;             
  gotoxy(31,2);write('KINGDOM OF KROZ II');
  gotoxy(26,3);writeln('An Apogee Software Production');
  writeln;
  writeln('Other great games available from Scott Miller:');
  writeln;col(15,15);
  writeln('� Six more Kroz games!  KINGDOM OF KROZ I, CAVERNS OF KROZ, DUNGEONS OF KROZ,');
  writeln('     RETURN TO KROZ, TEMPLE OF KROZ and THE FINAL CRUSADE OF KROZ.');
  writeln('     Each volume is just $7.50, or order all six for $35!');
  writeln;col(15,15);
  writeln('� THE LOST ADVENTURES OF KROZ - All-new seventh Kroz game with 75 of the best');
  write  ('     levels yet!  Built-in contest!  New features galore.  ($20)');
  cur(2);col(7,7);
  ClearKeys;
  HALT;
 end; { Sign_Off }

procedure Shareware(Wait: boolean);
 begin
  bak(1,0);bor(1);clrscr;cur(3);col(15,15);
  gotoxy(22,1);
  writeln('KINGDOM OF KROZ II � HOW TO REGISTER');
  gotoxy(1,2);
  for x:=1 to 80 do write('�');
  gotoxy(1,3);
  col(7,7);
  writeln('  This is a shareware game, meaning it''s user-supported.  If you enjoy this');
  writeln('game you are asked by the author to please send a registration check in the');
  writeln('amount of $7.50 to Apogee Software.');
  writeln('  This registration fee will qualify you to order any of the other Kroz');
  writeln('volumes available:');
  writeln;col(15,7);
  writeln('  � Caverns of Kroz   - the first discovery of Kroz');
  writeln('  � Dungeons of Kroz  - the dark side of Kroz, fast-paced action');
  writeln('  � Kingdom of Kroz I - the national contest winner ("Best Game" in 1988)');
  writeln('  � Return to Kroz    - the discovery of entirely new underground chambers');
  writeln('  � Temple of Kroz    - the bizarre side of Kroz, nothing is what it seems');
  writeln('  � The Final Crusade of Kroz - the surprising finish?');
  writeln;col(7,7);
  writeln('Each game is priced $7.50 each, any three for $20, or all six for only $35.');
  writeln('You''ll also get a secret code that makes this game easier to complete,');
  writeln('plus a "Hints, Tricks and Scoring Secrets" guide and "The Domain of Kroz" map.');
  writeln;col(7,7);
  write('Please make checks payable to:');
  col(14,7);
  writeln('   Apogee Software    (phone: 214/240-0614)');gotoxy(31,21);
  writeln('   4206 Mayflower');col(15,15);
  write  ('Address always valid!');gotoxy(31,22);col(14,7);
  writeln('   Garland, TX 75043  (USA)');
  writeln;
  col(7,7);
  write('Thank you and enjoy the game.  -- Scott Miller');
  if Wait then delay(0);
  bak(random(6)+1,7);
  gotoxy(1,25);
  insline;
  gotoxy(27,25);
  col(16,16);
  write('Press any key to continue.');
  ClearKeys;
  repeat x:=random(maxint) until keypressed;
  ClearKeys;
  bak(0,0);bor(4);clrscr;cur(3);
 end; { Shareware }

procedure New_Gem_Color;
 begin
  repeat
   GemColor:=random(15)+1;
   if not Color then GemColor := 7;
  until GemColor <> 8;
 end;

procedure Play(Start,Stop,Speed:integer);
  var x:integer;
 begin
  if Start<=Stop then
   for x:=Start to Stop do begin sound(x);delay(Speed)end
  else
   for x:=Start downto Stop do begin sound(x);delay(Speed) end;
  nosound;
 end; { Play }

procedure AddScore(What:integer);
 begin
  case What of
   {Monsters}  1..3:Score:=Score+What;
   {Block}     4,14:if Score > 2 then Score:=Score-2;
   {Whip}      5:Score:=Score+1;
   {Stairs}    6:Score:=Score+Level;
   {Chest}     7:Score:=Score+5;
   {Gem}       9:Score:=Score+1;
   {Invisible} 10:Score:=Score+10;
   {Teleport}  11:Score:=Score+1;
   {SpeedTime} 15:Score:=Score+2;
   {Trap}      16:if Score>5 then Score:=Score-5;
   {Lava}      22:Score:=Score+25;
   {Border}    20:if Score > Level then Score:=Score-(Level div 2);
   {Nugget}    27:Score:=Score+50;
   {Create}    35:Score:=Score+Level*2;
   {Generator} 36:Score:=Score+50;
   {MBlock}    38:Score:=Score+1;
  end;
  Update_Info;
 end; { AddScore }

procedure Won;
 begin
  Border;
  ClearKeys;
  col(15,31);bak(BB,0); 
  print(5,1,'YOUR QUEST FOR THE MAGICAL AMULET OF KROZ WAS SUCCESSFUL!!');
  bak(0,0);
  High_Score(false);
 end; { Dead }

procedure High_Score(PlayAgain:boolean);
  var x,
      Place : integer;
      Stop  : boolean;
 begin
  ClearKeys;
  window(2,2,XSize+1,YSize+1);
  bak(0,0);clrscr;
  window(1,1,80,25);
  cur(3);
  assign(HSFile,'KINGDOM2.HS');
  {$I-}
  reset(HSFile);
  {$I+}
  if IOResult <> 0 then
   begin
    rewrite(HSFile);
    for x:=1 to 15 do
     with HSList[x] do
      begin
       case x of
        1:begin Name:='Scott Miller';HighScore:=13640;HighLevel:=16;end;
        2:begin Name:='I. Jones';HighScore:=8574;HighLevel:=14;end;
        3:begin Name:='Terry Nagy';HighScore:=6995;HighLevel:=11;end;
        4:begin Name:='Cmdr. Keen';HighScore:=3501;HighLevel:=8;end;
        5:begin Name:='Banzai Boyd';HighScore:=1228;HighLevel:=5;end
        else begin Name:='Adventurer';HighScore:=0;HighLevel:=0;end
       end;
       write(HSFile,HSList[x]);
      end;
    close(HSFile);
   end;
  col(9,9);
  gotoxy(25,3);
  write('KINGDOM OF KROZ II');
  col(11,7);
  gotoxy(16,5);write('NAME');
  gotoxy(34,5);write('HIGH SCORE');
  gotoxy(49,5);write('LEVEL');
  reset(HSFile);
  for x:=1 to 15 do
   read(HSFile,HSList[x]);
  Place:=1;
  Stop:=false;
  repeat
   if Score>HSList[Place].HighScore then Stop:=true;
   Place:=Place+1;
   if not Stop and (Place>15) then Place:=100;
  until Stop or (Place>15);
  Place:=Place-1;
  if Place<16 then
   for x:=15 downto Place do
    HSList[x]:=HSList[x-1];
  with HSList[Place] do
   begin
    Name:='';
    HighScore:=Score;
    HighLevel:=Level;
   end;
  for x:=1 to 15 do
   begin
    if odd(x) then col(12,7) else col(13,7);
    with HSList[x] do
     begin
      gotoxy(13,x+6);write(x:2);
      gotoxy(16,x+6);write(Name);
      gotoxy(36,x+6);write(HighScore);if HighScore>0 then write('0');
      gotoxy(50,x+6);write(HighLevel);
     end;
   end;
  close(HSFile);
  ClearKeys;
  if Place<16 then
   begin
    bak(4,7);
    gotoxy(16,Place+6);
    write('               ');
    col(4,0);
    bak(7,7);
    gotoxy(16,23);
    write('Enter your name then press <enter>.');
    col(15,15);
    bak(4,7);
    gotoxy(16,Place+6);
    cur(2);
    readln(HSList[Place].Name);
    cur(3);
    rewrite(HSFile);
    for x:=1 to 15 do write(HSFile,HSList[x]);
    close(HSFile);
   end;
  bak(0,0);
  gotoxy(16,23);
  write('                                   ');
  for x:=1 to 999 do
   begin
    SX[x]:=0;SY[x]:=0;
    MX[x]:=0;MY[x]:=0;
    FX[x]:=0;FY[x]:=0;
    BX[x]:=0;BY[x]:=0;
   end;
  if PlayAgain then
   Flash(14,25,'Do you want to play another game (Y/N)?')
  else
   begin
    ch:='N';
    Flash(21,25,'Press any key to continue.');
   end;
  if PlayAgain then read(kbd,ch);
  if upcase(ch) <> 'N' then Restart:=true
  else
   begin
    bak(0,0);col(15,15);bor(0);cur(1);
    clrscr;
    if not PlayAgain then
     begin
      gotoxy(1,2);
      writeln('You''ve completed KINGDOM OF KROZ II!');
     end
    else
     begin
      gotoxy(17,2);
      writeln('KINGDOM OF KROZ II');
     end;
    Sign_Off;
   end;
 end; { High_Score }

procedure Dead(DeadDot: boolean);
 begin
  if Gems>9 then col(4,7)
  else
   begin Gems:=0;col(20,23);end;
  bak(7,0);
  gotoxy(71,8);
  write('     ');
  str(Gems,StrVal);
  gotoxy(73-length(StrVal) div 2,8);
  write(StrVal);
  bak(0,0);
  if DeadDot then
   for x:=150 downto 5 do
    begin
     gotoxy(PX,PY);
     col(x,x);bak(random(8),0);
     write(Player);
     sound(x*x);
    end;
  nosound;
  ClearKeys;
  col(16,16);bak(BB,7);
  print(27,1,'YOU HAVE DIED!!');
  bak(0,0);
  repeat
   col(random(16),random(16));
   gotoxy(PX,PY);
   if DeadDot then write('*');
   print(21,25,'Press any key to continue.');
  until keypressed;
  Border;
  High_Score(true);
 end; { Dead }

procedure Define_Levels;
 begin

DF[3]:=
{  1  2  3  X  W  L  C  S  +  I  T  K  D  #  F  .  R  Q  /  \  B  V  =  A  U  Z  *  E  ;  :  `  -  @  %  ]  G  (  M  )}
' 80       50     1                      30                                                                           '+
{  P  &  !  O  H  ?  >  N  <  [  |  "  4  5  6  7  8  9  �  �  �  �  �  �  Y  0  ~  $}
'                                                                                    '+
{  �  �  �  �  �  �  �}
'  9                  ';

DF[5]:=
{  1  2  3  X  W  L  C  S  +  I  T  K  D  #  F  .  R  Q  /  \  B  V  =  A  U  Z  *  E  ;  :  `  -  @  %  ]  G  (  M  )}
'100          30  1        9     2                                                                                    '+
{  P  &  !  O  H  ?  >  N  <  [  |  "  4  5  6  7  8  9  �  �  �  �  �  �  Y  0  ~  $}
'                                                                        900         '+
{  �  �  �  �  �  �  �}
'  5                  ';
  
DF[7]:=
{  1  2  3  X  W  L  C  S  +  I  T  K  D  #  F  .  R  Q  /  \  B  V  =  A  U  Z  *  E  ;  :  `  -  @  %  ]  G  (  M  )}
'         976 20  3  2     9            320     9             20                 9                                    '+
{  P  &  !  O  H  ?  >  N  <  [  |  "  4  5  6  7  8  9  �  �  �  �  �  �  Y  0  ~  $}
'                       3  2  2  2  2                                                '+
{  �  �  �  �  �  �  �}
'                 9   ';

DF[9]:=
{  1  2  3  X  W  L  C  S  +  I  T  K  D  #  F  .  R  Q  /  \  B  V  =  A  U  Z  *  E  ;  :  `  -  @  %  ]  G  (  M  )}
' 50          90  2  2                         25     1200 50                   55                                    '+
{  P  &  !  O  H  ?  >  N  <  [  |  "  4  5  6  7  8  9  �  �  �  �  �  �  Y  0  ~  $}
'        1                 1  1  1  1                                                '+
{  �  �  �  �  �  �  �}
'                     ';

DF[11]:=
{  1  2  3  X  W  L  C  S  +  I  T  K  D  #  F  .  R  Q  /  \  B  V  =  A  U  Z  *  E  ;  :  `  -  @  %  ]  G  (  M  )}
'100              2       45                                               8   100  3                                 '+
{  P  &  !  O  H  ?  >  N  <  [  |  "  4  5  6  7  8  9  �  �  �  �  �  �  Y  0  ~  $}
'                                                                           100600   '+
{  �  �  �  �  �  �  �}
'                     ';

DF[13]:=
{  1  2  3  X  W  L  C  S  +  I  T  K  D  #  F  .  R  Q  /  \  B  V  =  A  U  Z  *  E  ;  :  `  -  @  %  ]  G  (  M  )}
'350          20  2     9 40                                                    20  1                       3         '+
{  P  &  !  O  H  ?  >  N  <  [  |  "  4  5  6  7  8  9  �  �  �  �  �  �  Y  0  ~  $}
'     1                                                                              '+
{  �  �  �  �  �  �  �}
' 30                  ';

DF[15]:=
{  1  2  3  X  W  L  C  S  +  I  T  K  D  #  F  .  R  Q  /  \  B  V  =  A  U  Z  *  E  ;  :  `  -  @  %  ]  G  (  M  )}
'                 4                                             300            500 20                                 '+
{  P  &  !  O  H  ?  >  N  <  [  |  "  4  5  6  7  8  9  �  �  �  �  �  �  Y  0  ~  $}
'                          2  2  2  2                                                '+
{  �  �  �  �  �  �  �}
'                     ';

DF[17]:=
{  1  2  3  X  W  L  C  S  +  I  T  K  D  #  F  .  R  Q  /  \  B  V  =  A  U  Z  *  E  ;  :  `  -  @  %  ]  G  (  M  )}
'                 1                                                                                     15            '+
{  P  &  !  O  H  ?  >  N  <  [  |  "  4  5  6  7  8  9  �  �  �  �  �  �  Y  0  ~  $}
'                 1                                                                  '+
{  �  �  �  �  �  �  �}
'                     ';

DF[19]:=
{  1  2  3  X  W  L  C  S  +  I  T  K  D  #  F  .  R  Q  /  \  B  V  =  A  U  Z  *  E  ;  :  `  -  @  %  ]  G  (  M  )}
'600          20  1     5 30     5                                              20  5                           700   '+
{  P  &  !  O  H  ?  >  N  <  [  |  "  4  5  6  7  8  9  �  �  �  �  �  �  Y  0  ~  $}
'                                                                                    '+
{  �  �  �  �  �  �  �}
'                     ';

DF[21]:=
{  1  2  3  X  W  L  C  S  +  I  T  K  D  #  F  .  R  Q  /  \  B  V  =  A  U  Z  *  E  ;  :  `  -  @  %  ]  G  (  M  )}
' 40              3                            30                               80                    2               '+
{  P  &  !  O  H  ?  >  N  <  [  |  "  4  5  6  7  8  9  �  �  �  �  �  �  Y  0  ~  $}
'                          1  1  1  1                                       800      '+
{  �  �  �  �  �  �  �}
'                     ';

DF[23]:=
{  1  2  3  X  W  L  C  S  +  I  T  K  D  #  F  .  R  Q  /  \  B  V  =  A  U  Z  *  E  ;  :  `  -  @  %  ]  G  (  M  )}
'                 1                                                                                         3         '+
{  P  &  !  O  H  ?  >  N  <  [  |  "  4  5  6  7  8  9  �  �  �  �  �  �  Y  0  ~  $}
'                          1  1  1  1                                                '+
{  �  �  �  �  �  �  �}
' 70 50  9 25  9 18   ';

 end; { Define_Levels }

procedure Convert_Format;
  var XLoop,
      YLoop  : integer;
      tempstr: string[1];
 begin
  SNum:=Null; MNum:=Null; FNum:=Null; BNum:=Null; GenNum:=Null;
  T[9]:=-1; LavaFlow:=false;TreeRate:=0;GravCounter:=0;GravOn:=false;
  for x:=1 to 66 do for y:=1 to 25 do PF[x,y]:=0;
  for x:=1 to 999 do
   begin                        {* reset monster's X, Y *}
    SX[x]:=0;SY[x]:=0;
    MX[x]:=0;MY[x]:=0;
    FX[x]:=0;FY[x]:=0;
   end;
  for x:=1 to 1300 do begin BX[x]:=0;BY[x]:=0; end;
  New_Gem_Color;
  for YLoop:=1 to YSize do
   for XLoop:=1 to XSize do
    begin
    tempstr := copy(FP[YLoop], XLoop, 1);

    // Basic syntax. Whatever is inside of the '' is assigned(:=) the ASCII  character...
    // after the = signed. 
    // PF is a 2 dimensional loop that places the character in the screen.
    
    case char(tempstr[1]) of // Switch-statement
    // Takes the first character of tempstr var and converts it into a char if not already
     ' ':PF[XLoop+1,YLoop+1]:=Null;
     '1':begin
          SNum:=SNum+1;SX[SNum]:=XLoop+1;SY[SNum]:=YLoop+1;
          PF[XLoop+1,YLoop+1]:=1;
         end;
     '2':begin
          MNum:=MNum+1;MX[MNum]:=XLoop+1;MY[MNum]:=YLoop+1;
          PF[XLoop+1,YLoop+1]:=2;
         end;
     '3':begin
          FNum:=FNum+1;FX[FNum]:=XLoop+1;FY[FNum]:=YLoop+1;
          PF[XLoop+1,YLoop+1]:=3;
         end;
     'X':PF[XLoop+1,YLoop+1]:=4;
     'W':PF[XLoop+1,YLoop+1]:=5;
     'L':PF[XLoop+1,YLoop+1]:=6;
     'C':PF[XLoop+1,YLoop+1]:=7;
     'S':PF[XLoop+1,YLoop+1]:=8;
     '+':PF[XLoop+1,YLoop+1]:=9;
     'I':PF[XLoop+1,YLoop+1]:=10;
     'T':PF[XLoop+1,YLoop+1]:=11;
     'K':PF[XLoop+1,YLoop+1]:=12;
     'D':PF[XLoop+1,YLoop+1]:=13;
     '#':PF[XLoop+1,YLoop+1]:=14;
     'F':PF[XLoop+1,YLoop+1]:=15;
     '.':PF[XLoop+1,YLoop+1]:=16;
     'R':PF[XLoop+1,YLoop+1]:=17;
     'Q':PF[XLoop+1,YLoop+1]:=18;
     '/':PF[XLoop+1,YLoop+1]:=19;
     '\':PF[XLoop+1,YLoop+1]:=20;
     'B':PF[XLoop+1,YLoop+1]:=21;
     'V':PF[XLoop+1,YLoop+1]:=22;
     '=':PF[XLoop+1,YLoop+1]:=23;
     'A':PF[XLoop+1,YLoop+1]:=24;
     'U':PF[XLoop+1,YLoop+1]:=25;
     'Z':PF[XLoop+1,YLoop+1]:=26;
     '*':PF[XLoop+1,YLoop+1]:=27;
     'E':PF[XLoop+1,YLoop+1]:=28;
     ';':PF[XLoop+1,YLoop+1]:=29;
     ':':PF[XLoop+1,YLoop+1]:=30;
     '`':PF[XLoop+1,YLoop+1]:=31;
     '-':PF[XLoop+1,YLoop+1]:=32;
     '@':PF[XLoop+1,YLoop+1]:=33;
     '%':PF[XLoop+1,YLoop+1]:=34;
     ']':PF[XLoop+1,YLoop+1]:=35;
     'G':begin PF[XLoop+1,YLoop+1]:=36;GenNum:=GenNum+1;end;
     '(':PF[XLoop+1,YLoop+1]:=37;
     'M':begin
          BNum:=BNum+1;BX[BNum]:=XLoop+1;BY[BNum]:=YLoop+1;
          PF[XLoop+1,YLoop+1]:=38;
         end;
     ')':PF[XLoop+1,YLoop+1]:=39;
     'P':begin PF[XLoop+1,YLoop+1]:=40;PX:=XLoop+1;PY:=YLoop+1;end;
     '&':PF[XLoop+1,YLoop+1]:=41;
     '!':PF[XLoop+1,YLoop+1]:=42;
     'O':PF[XLoop+1,YLoop+1]:=43;
     'H':PF[XLoop+1,YLoop+1]:=44;
     '?':PF[XLoop+1,YLoop+1]:=45;
     '>':begin PF[XLoop+1,YLoop+1]:=46;T[9]:=32000;end; 
     'N':PF[XLoop+1,YLoop+1]:=47;
     '<':PF[XLoop+1,YLoop+1]:=48;
     '[':PF[XLoop+1,YLoop+1]:=49;
     '|':PF[XLoop+1,YLoop+1]:=50;
     '"':PF[XLoop+1,YLoop+1]:=51;
     '4':PF[XLoop+1,YLoop+1]:=52;
     '5':PF[XLoop+1,YLoop+1]:=53;
     '6':PF[XLoop+1,YLoop+1]:=54;
     '7':PF[XLoop+1,YLoop+1]:=55;
     '8':PF[XLoop+1,YLoop+1]:=56;
     '9':PF[XLoop+1,YLoop+1]:=57;
     '�':PF[XLoop+1,YLoop+1]:=58;
     '�':PF[XLoop+1,YLoop+1]:=59;
     '�':PF[XLoop+1,YLoop+1]:=60;
     '�':PF[XLoop+1,YLoop+1]:=61;
     '�':PF[XLoop+1,YLoop+1]:=62;
     '�':PF[XLoop+1,YLoop+1]:=63;
     'Y':PF[XLoop+1,YLoop+1]:=64;
     '0':PF[XLoop+1,YLoop+1]:=65;
     '~':PF[XLoop+1,YLoop+1]:=66;
     '$':PF[XLoop+1,YLoop+1]:=67;
     '�':PF[XLoop+1,YLoop+1]:=68;
     '�':PF[XLoop+1,YLoop+1]:=69;
     '�':PF[XLoop+1,YLoop+1]:=70;
     '�':PF[XLoop+1,YLoop+1]:=71;
     '�':PF[XLoop+1,YLoop+1]:=72;
     '�':PF[XLoop+1,YLoop+1]:=73;
     '�':PF[XLoop+1,YLoop+1]:=74;
     '�':PF[XLoop+1,YLoop+1]:=75;
     '�':PF[XLoop+1,YLoop+1]:=76;
     '�':PF[XLoop+1,YLoop+1]:=77;
     '�':PF[XLoop+1,YLoop+1]:=78;
     '�':PF[XLoop+1,YLoop+1]:=79;
     '�':PF[XLoop+1,YLoop+1]:=80;
     '�':PF[XLoop+1,YLoop+1]:=81;
     '�':PF[XLoop+1,YLoop+1]:=180;
     '�':PF[XLoop+1,YLoop+1]:=181;
     '�':PF[XLoop+1,YLoop+1]:=182;
     '�':PF[XLoop+1,YLoop+1]:=183;
     '�':PF[XLoop+1,YLoop+1]:=184;
     '�':PF[XLoop+1,YLoop+1]:=224;
     '�':PF[XLoop+1,YLoop+1]:=225;
     '�':PF[XLoop+1,YLoop+1]:=226;
     '�':PF[XLoop+1,YLoop+1]:=227;
     '�':PF[XLoop+1,YLoop+1]:=228;
     '�':PF[XLoop+1,YLoop+1]:=229;
     '�':PF[XLoop+1,YLoop+1]:=230;
     '�':PF[XLoop+1,YLoop+1]:=231;
     '�':PF[XLoop+1,YLoop+1]:=82;
     '�':PF[XLoop+1,YLoop+1]:=83;
     '�':PF[XLoop+1,YLoop+1]:=252
     else
      begin
       tempstr := copy(FP[YLoop], XLoop, 1);
       PF[XLoop+1,YLoop+1]:=ord(char(tempstr[1]));
      end;
    end;
    end;
 end; { Convert_Format }

procedure Go(var XWay,YWay:integer; Human:boolean);
  var Previous, OldX, OldY: integer;
  label JUMP;
 begin
  if (Sideways)and(YWay=-1)and(not OneMove)and(Replacement<>75) then goto JUMP;
  Previous:=Replacement; OldX:=PX; OldY:=PY;
  PF[PX,PY]:=Replacement;
  gotoxy(PX,PY);
  write(' ');
  PX:=PX+XWay;PY:=PY+YWay;
  if PF[PX,PY] in [55..57,75] then Replacement:=PF[PX,PY]
  else                             Replacement:=Null;
  if Previous=75 then
   begin
    col(7,7);
    gotoxy(OldX,OldY);
    write(Rope);
   end;
  PF[PX,PY]:=40;
  if T[5]<1 then
   begin
    gotoxy(PX,PY);col(14,15);bak(0,0);
    write(Player);
   end
  else begin gotoxy(PX,PY);write(' ');end;
 if not Sideways then FootStep
 else if (Replacement <> 75) and Human then FootStep;
 if keypressed and Human then
  begin
   read(kbd,ch);
   if ch=#27 then read(kbd,ch);
  end;
  JUMP:
 end; { Go }

procedure MoveRock(var XWay,YWay:integer);
 begin
  for i:=1 to ord(FastPC)*500+ord(not FastPC)*330 do
   begin sound(random(100)+20);delay(1);end; nosound;
  gotoxy(PX+XWay,PY+YWay);
  col(0,0);
  write(' ');
  gotoxy(RX,RY);
  col(7,7);
  write(Rock);
  PF[RX,RY]:=65;
  Go(XWay,YWay,PMove);
  SKipTime:=3001;
 end;

procedure Trigger_Trap(Place:boolean; i:integer; ch:char);
 begin
  if (PF[PX-1,PY-1] in [0,32,33,37,39,41,47,67..74,224..231])and(PX-1>1)and(PY-1>1) then
   begin gotoxy(PX-1,PY-1);write(ch);if Place then PF[PX-1,PY-1]:=i;end;delay(5);
  if (PF[PX,PY-1] in [0,32,33,37,39,41,47,67..74,224..231])and(PY-1>1) then
   begin gotoxy(PX,PY-1);write(ch);if Place then PF[PX,PY-1]:=i;end;delay(5);
  if (PF[PX+1,PY-1] in [0,32,33,37,39,41,47,67..74,224..231])and(PX+1<66)and(PY-1>1) then
   begin gotoxy(PX+1,PY-1);write(ch);if Place then PF[PX+1,PY-1]:=i;end;delay(5);
  if (PF[PX+1,PY] in [0,32,33,37,39,41,47,67..74,224..231])and(PX+1<66) then
   begin gotoxy(PX+1,PY);write(ch);if Place then PF[PX+1,PY]:=i;end;delay(5);
  if (PF[PX+1,PY+1] in [0,32,33,37,39,41,47,67..74,224..231])and(PX+1<66)and(PY+1<25) then
   begin gotoxy(PX+1,PY+1);write(ch);if Place then PF[PX+1,PY+1]:=i;end;delay(5);
  if (PF[PX,PY+1] in [0,32,33,37,39,41,47,67..74,224..231])and(PY+1<25) then
   begin gotoxy(PX,PY+1);write(ch);if Place then PF[PX,PY+1]:=i;end;delay(5);
  if (PF[PX-1,PY+1] in [0,32,33,37,39,41,47,67..74,224..231])and(PX-1>1)and(PY+1<25) then
   begin gotoxy(PX-1,PY+1);write(ch);if Place then PF[PX-1,PY+1]:=i;end;delay(5);
  if (PF[PX-1,PY] in [0,32,33,37,39,41,47,67..74,224..231])and(PX-1>1) then
   begin gotoxy(PX-1,PY);write(ch);if Place then PF[PX-1,PY]:=i;end;delay(5);
 end; { Trigger_Trap }

procedure End_Routine;
 begin
  FootStep;
  delay(300);
  FootStep;
  delay(300);
  FootStep;
  for x:=1 to ord(FastPC)*2650+ord(not FastPC)*250 do
   begin
    sound(random(3000)+x);
    gotoxy(PX,PY);
    bak(random(8),0);
    col(14,15);
    write(Player);
    col(random(16),random(16));
    bak(0,0);
    print(15,25,'Oh no, something strange is happening!');
   end;
  for i:=ord(FastPC)*9000+ord(FastPC)*2200 downto 20 do sound(random(i));
  col(14,15);bak(0,0);
  for x:=1 to ord(FastPC)*3500+ord(not FastPC)*650 do
   begin
    sound(x*3);
    gotoxy(PX,PY);
    write(chr(220+random(4)));
   end;
  nosound;
  gotoxy(PX,PY);
  col(16,16);
  bak(2,7);
  write(Stairs);
  Restore_Border;
  Flash(14,25,'You are magically transported from Kroz!');
  ClearKeys;
  col(15,15);bak(0,0);
  print(15,25,'Your Gems are worth 100 points each...');
  for i:=1 to Gems do
   begin
    sound(i*8+100); Score:=Score+10; Update_Info; delay(20);
   end; nosound; 
  read(kbd,ch);
  Restore_Border;
  ClearKeys;
  col(15,15);bak(0,0);
  print(15,25,'Your Whips are worth 100 points each...');
  for i:=1 to Whips do
   begin
    sound(i*10+200); Score:=Score+10; Update_Info; delay(20);
   end; nosound; 
  read(kbd,ch);
  Restore_Border;
  ClearKeys;
  col(15,15);bak(0,0);
  print(9,25,'Your Teleport Scrolls are worth 200 points each...');
  for i:=1 to Teleports do
   begin
    sound(i*12+300); Score:=Score+20; Update_Info; delay(30);
   end; nosound; 
  read(kbd,ch);
  Restore_Border;
  ClearKeys;
  col(15,15);bak(0,0);
  print(14,25,'Your Keys are worth 10,000 points each...');
  for i:=1 to Keys do
   begin
    sound(i*30+100); Score:=Score+1000; Update_Info; delay(50);
   end; nosound; 
  read(kbd,ch);
  Restore_Border;
  ClearKeys;
  bak(GemColor,7);
  for x:=1 to 30 do
   begin
    window(32-x,12-(x div 3),35+x,14+(x div 3));
    clrscr;
   end;
  bak(0,0);
  for x:=1 to 30 do
   begin
    window(32-x,12-(x div 3),35+x,14+(x div 3));
    clrscr;
    sound(x*45);
   end; nosound;
  window(1,1,80,25);cur(3);
  bak(1,0);window(2,2,65,24);
  clrscr;
  col(14,15);
  gotoxy(25,2);
  writeln('BACK AT YOUR HUT');
  gotoxy(25,3);
  writeln('����������������');
  writeln;
  col(15,7);
  { 15 writeln's available for text }
  writeln('   For years you''ve waited for such a wonderful archaeological');
  writeln(' discovery. And now you possess one of the greatest finds ever!');
  writeln('   The Magical Amulet will bring you great fame, and even more');
  writeln(' so if you ever learn how to harness the Amulet''s magical');
  writeln(' abilities.  For now it must wait, though, for Kroz is a huge');
  writeln(' place, and still mostly unexplored.');
  writeln('   Even with the many dangers that await, you feel another');
  writeln(' expedition is in order.  You must leave no puzzle unsolved, no');
  writeln(' treasure unfound--to quit now would leave the job unfinished.');
  writeln('   So you plan for a good night''s rest, and think ahead to');
  writeln(' tomorrow''s new journey.  What does the mysterious kingdom of');
  writeln(' Kroz have waiting for you, what type of new creatures will');
  writeln(' try for your blood, and what kind of brilliant treasure does');
  writeln(' Kroz protect.  Tomorrow will tell...');
  writeln;col(14,15);
  writeln('                         RETURN TO KROZ');col(15,7);
  write  ('        ( Now available -- $7.50 or write for details. )');
  ClearKeys;
  window(1,1,80,25);bak(0,0);
  Flash(21,25,'Press any key, Adventurer.');
  WON;
 end; {End_Routine }

begin
end. { Levels }
