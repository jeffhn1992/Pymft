inputWeight = input("Please input your weight")
inputHeight = input("Please input your height")
inputWeightInt = float(inputWeight)
inputHeightInt = float(inputHeight)
bmi = inputWeightInt / (inputHeightInt * inputHeightInt)
if bmi <= 18:
    print("Under Weight")
elif bmi <= 25:
    print("Normal")
elif bmi <= 30:
    print("Over Weight")
elif bmi < 30:
    print("Obese")

