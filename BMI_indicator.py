#Women list insert
W_height_list = []
W_weight_list = []
W_BMI_list = []
W_i = 1
W_j = 0
print("\n        ==== Welcome to BMI calculator ====")
#Get number of women to ba calculate
W_Number = int(input("\nPlease enter No. of women you want to calculate BMI =: "))
print("\n  ==== Please enter Height and weight of women ====")
#Get women data
while W_i <= W_Number:
    List1value = float(input("\nEnter height in meters of women no.%d =: " % W_i))
    W_height_list.append(List1value)
    List2value = float(input("Enter weight in kilograms of women no.%d =: " % W_i))
    W_weight_list.append(List2value)
    W_i = W_i + 1
#Calculate women BMI
while W_j < W_Number:
    W_BMI_list.append(W_weight_list[W_j] / (W_height_list[W_j]*W_height_list[W_j]))
    W_j = W_j + 1
#Display women BMI
print("\n--->The BMI of", W_Number, "women")
for i in range(len(W_BMI_list)):
    print("->Women BMI of no.", i+1, end=" = ")
    print(f"{W_BMI_list[i]:.2f}")
#Calcualate and Display average of women BMI
W_BMI_avg = sum(W_BMI_list)/len(W_BMI_list)
print("--->The average BMI of", W_Number, "women is = ", round(W_BMI_avg, 2))
#*************************************************************************************
#Men list insert
M_height_list = []
M_weight_list = []
M_BMI_list = []
M_i = 1
M_j = 0
#Get number of men to ba calculate
M_Number = int(input("\nPlease enter No. of men you want to calculate BMI =: "))
print("\n  ==== Please enter Height and weight of men ====")
#Get men data
while M_i <= M_Number:
    List1value = float(input("\nEnter height in meters of men no.%d =: " % M_i))
    M_height_list.append(List1value)
    List2value = float(input("Enter weight in kilograms of men no.%d =: " % M_i))
    M_weight_list.append(List2value)
    M_i = M_i + 1
#Calculate men BMI
while M_j < M_Number:
    M_BMI_list.append(M_weight_list[M_j] / (M_height_list[M_j]*M_height_list[M_j]))
    M_j = M_j + 1
#Display men BMI
print("\n--->The BMI of", M_Number, "men")
for i in range(len(M_BMI_list)):
    print("->Men BMI of no.", i+1, end=" = ")
    print(f"{M_BMI_list[i]:.2f}")
#Calcualate and Display average of men BMI
M_BMI_avg = sum(M_BMI_list)/len(M_BMI_list)
print("--->The average BMI of", M_Number, "men is = ", round(M_BMI_avg, 2))
#******************************************************************************************
#Calculate and Display BMI for all women and men
Both_BMI_avg = (sum(M_BMI_list)+sum(W_BMI_list)) / (len(M_BMI_list)+len(W_BMI_list))
print("\n****************************************************************")
print("*--->The average BMI for both all women and men is", round(Both_BMI_avg, 4), "<---*")
if Both_BMI_avg < 16:
    print("*               ==The BMI is Severe Thinness==                 *")

elif Both_BMI_avg >= 16 and Both_BMI_avg < 17:
    print("*              ==The BMI is Moderate Thinness==                *")

elif Both_BMI_avg >= 17 and Both_BMI_avg < 18.5:
    print("*                ==The BMI is Mild Thinness==                  *")

elif Both_BMI_avg >= 18.5 and Both_BMI_avg < 25:
    print("*                   ==The BMI is Normal==                      *")

elif Both_BMI_avg >= 25.5 and Both_BMI_avg < 30:
    print("*                 ==The BMI is Overweight==                    *")

elif Both_BMI_avg >= 30.5 and Both_BMI_avg < 35:
    print("*               ==The BMI is Obese Class I==                   *")

elif Both_BMI_avg >= 35.5 and Both_BMI_avg < 40:
    print("*               ==The BMI is Obese Class II==                  *")

elif Both_BMI_avg >= 40:
    print("*               ==The BMI is Obese Class III==                 *")
print("****************************************************************")
print("*                          BMI RANGE                           *")
print("****************************************************************")
print("*   Severe Thinness            *               <16             *")
print("*   Moderate Thinness          *              16-17            *")
print("*   Mild Thinness              *             17-18.5           *")
print("*   Normal                     *             18.5-25           *")
print("*   Overweight                 *             25.5-30           *")
print("*   Obese Class I              *             30.5-35           *")
print("*   Obese Class II             *             35.5-40           *")
print("*   Obese Class III            *               >40             *")
print("****************************************************************")


