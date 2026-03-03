\ Model WorldLight_Optimization
\ LP format - for model browsing. Use MPS format to capture full model detail.
\ Signature: 0xac1ecdcb81a45966
Maximize
  Product1 + 2 Product2
Subject To
 Frame_Parts: Product1 + 3 Product2 <= 200
 Electrical_Components: 2 Product1 + 2 Product2 <= 300
 Max_Product2: Product2 <= 20
Bounds
End
