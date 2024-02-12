print ("FLUID MECHANICS Quiz-1 by Olutola Fakehinde - 26/10/2023")
Ready = input ("Are you ready for Quiz-1? ").lower()
if Ready != "yes":
    quit ()
print ("I am ready. Let's get started :)")
Score = 0
Ask = input ("QUESTION 1:  Fluid is the same as solid - Yes or No? ").lower()
if Ask == "no":
    print ("You are correct")
    Score += 1
else:
    print ('Oops! You are wrong! Answer is - No')

Ask = input ("QUESTION 2: Which of these is not a fluid - Liquid, Solid or Gas? ").lower()
if Ask == "solid":
    print ("You are correct")
    Score += 1
else:
    print ('Oops! You are wrong! The answer is - Solid')

Ask = input ("QUESTION 3: A fluid naturally flows upstream - True or False? ").lower()
if Ask == "false":
    print ("You are correct")
    Score += 1
else:
    print ('Oops! You are wrong! The answer is - False')

Ask = input ("QUESTION 4: A venturimeter measures flow rate - True or False? ").lower()
if Ask == "true":
    print ("You are correct")
    Score += 1
else:
    print ('Oops! You are wrong! The answer is - True')

Ask = input ("QUESTION 5: High velocity flow in a conduit of large size is laminar or turbulent? ").lower()
if Ask == "turbulent":
    print ("You are correct")
    Score += 1
else:
    print ('Oops! You are wrong!. The answer is - turbulent')

Ask = input ("QUESTION 6: The type of flow in which its properties are constant with respect to distance is uniform or non-uniform? ").lower()
if Ask == "uniform":
    print ("You are correct")
    Score += 1
else:
    print ('Oops! You are wrong! The right answer is: - uniform')

Ask = input ("QUESTION 7: The friction in fluid is known as viscosity - Yes or No? ").lower()
if Ask == "yes":
    print ("You are correct")
    Score += 1
else:
    print ('Oops! You are wrong! The answer is - Yes')

Ask = input ("QUESTION 8: The type of flow in which its properties change with respect to time is steady or unsteady? ").lower()
if Ask == "unsteady":
    print ("You are correct")
    Score += 1
else:
    print ('Oops! You are wrong! The answer is - unsteady')

Ask = input ("QUESTION 9: Which is always referred to as compressible fluid - Liquid or Gas? ").lower()
if Ask == "gas":
    print ("You are correct")
    Score += 1
else:
    print ('Oops! You are wrong! The answer is - Gas')

Ask = input ("QUESTION 10: Density is a ratio of mass:volume - Yes or No? ").lower()
if Ask == "yes":
    print ("You are correct")
    Score += 1
else:
    print ('Oops! You are wrong! The answer is - Yes')


print ("You got " + str(Score) + " out of 10" + " questions correct!")
print ("Your achievement " + "in Quiz-1 =" + str(( Score / 10) * 100) + "%")
print ("Watch out for FLUID MECHANICS Quiz-2 by Olutola Fakehinde")
