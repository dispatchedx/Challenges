# Write a string representing a regular expression to detect whether a binary number is divisible by 7
# It won't be accepted if you code something else like Function
#solution = '^(0|1((101*0|00(01)*1)(10|11(01)*0(01)*00))*11|(101*0|11(01)*0(01)*00)01)*$'
#solution='(0|1((101*0|0(01)*1)10)*11|)*$'
#jflap
solution = '(0|111|100((1|00)0)*011|(101|100((1|00)0)*(1|00)1)(1((1|00)0)*(1|00)1)*(01|1((1|00)0)*011)|(110|100((1|00)0)*010|(101|100((1|00)0)*(1|00)1)(1((1|00)0)*(1|00)1)*(00|1((1|00)0)*010))(1|0(1((1|00)0)*(1|00)1)*(00|1((1|00)0)*010))*0(1((1|00)0)*(1|00)1)*(01|1((1|00)0)*011))+$'