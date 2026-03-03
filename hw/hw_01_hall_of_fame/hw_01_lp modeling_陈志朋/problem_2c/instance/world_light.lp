\ Model World_Light
\ LP format - for model browsing. Use MPS format to capture full model detail.
\ Signature: 0xac1ecdcb81a45484
Maximize
  Product1 + 2 Product2
Subject To
 Frame_parts: Product1 + 3 Product2 <= 200
 Electrical_components: 2 Product1 + 2 Product2 <= 300
 Product2_Num_Limit: Product2 <= 20
Bounds
End
