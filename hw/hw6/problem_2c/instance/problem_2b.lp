\ Model Computer_Purchase_Optimization
\ LP format - for model browsing. Use MPS format to capture full model detail.
\ Signature: 0x8f82c1143941e9ab
Minimize
  5000 whether_purchase_from_Vendor_1 + 4000 whether_purchase_from_Vendor_2
   + 6000 whether_purchase_from_Vendor_3 + [
   1000 whether_purchase_from_Vendor_1 * Number_purchased_from_Vendor_1
   + 700 whether_purchase_from_Vendor_2 * Number_purchased_from_Vendor_2
   + 500 whether_purchase_from_Vendor_3 * Number_purchased_from_Vendor_3
   ] / 2 
Subject To
 nonnegative_purchase_number_from_Vendor_1: Number_purchased_from_Vendor_1
   >= 0
 min_purchase_quantity_from_Vendor_1: - 200 whether_purchase_from_Vendor_1
   + Number_purchased_from_Vendor_1 >= 0
 max_purchase_quantity_from_Vendor_1: - 500 whether_purchase_from_Vendor_1
   + Number_purchased_from_Vendor_1 <= 0
 nonnegative_purchase_number_from_Vendor_2: Number_purchased_from_Vendor_2
   >= 0
 min_purchase_quantity_from_Vendor_2: - 200 whether_purchase_from_Vendor_2
   + Number_purchased_from_Vendor_2 >= 0
 max_purchase_quantity_from_Vendor_2: - 900 whether_purchase_from_Vendor_2
   + Number_purchased_from_Vendor_2 <= 0
 nonnegative_purchase_number_from_Vendor_3: Number_purchased_from_Vendor_3
   >= 0
 min_purchase_quantity_from_Vendor_3: - 200 whether_purchase_from_Vendor_3
   + Number_purchased_from_Vendor_3 >= 0
 max_purchase_quantity_from_Vendor_3: - 400 whether_purchase_from_Vendor_3
   + Number_purchased_from_Vendor_3 <= 0
 total_number_of_computers_planned_to_purchase:
   Number_purchased_from_Vendor_1 + Number_purchased_from_Vendor_2
   + Number_purchased_from_Vendor_3 = 1100
Bounds
Binaries
 whether_purchase_from_Vendor_1 whether_purchase_from_Vendor_2
 whether_purchase_from_Vendor_3
End
