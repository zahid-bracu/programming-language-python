is_male = False
is_tall = True

if is_male and is_tall:
    print("Tall and Dashing Boy")
elif not(is_male) and is_tall:
    print("Tall but beautiful Girl")
elif not(is_male) and not(is_tall):
    print("Short Girl")
elif is_male or is_tall:
    print("Male or Tall or both")
else:
    print("3rd Gender")