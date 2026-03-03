* Signature: 0xac1ecdcb81a45966
NAME WorldLight_Optimization
OBJSENSE MAX
ROWS
 N  OBJ
 L  Frame_Parts
 L  Electrical_Components
 L  Max_Product2
COLUMNS
    Product1  OBJ       1
    Product1  Frame_Parts  1
    Product1  Electrical_Components  2
    Product2  OBJ       2
    Product2  Frame_Parts  3
    Product2  Electrical_Components  2
    Product2  Max_Product2  1
RHS
    RHS1      Frame_Parts  200
    RHS1      Electrical_Components  300
    RHS1      Max_Product2  20
BOUNDS
ENDATA
