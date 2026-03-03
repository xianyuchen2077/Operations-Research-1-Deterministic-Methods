\ Model Tatham
\ LP format - for model browsing. Use MPS format to capture full model detail.
\ Signature: 0xd7e2b367139710b5
Maximize
  16000 Investment_1 + 8000 Investment_2 + 10000 Investment_3
   + 19500 Investment_4 + 22000 Investment_5 + 12000 Investment_6
   + 7500 Investment_7
Subject To
 Budget: 5000 Investment_1 + 2500 Investment_2 + 3500 Investment_3
   + 6000 Investment_4 + 7000 Investment_5 + 4500 Investment_6
   + 3000 Investment_7 <= 15000
Bounds
Binaries
 Investment_1 Investment_2 Investment_3 Investment_4 Investment_5
 Investment_6 Investment_7
End
