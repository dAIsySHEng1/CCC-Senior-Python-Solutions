b = input().split()
p = input().split()
blood = []
patient = []
for i in range(8):
    blood.append(int(b[i]))

for i in range(8):
    patient.append(int(p[i]))

maxhelp = 0
for i in range(8):
    minh = min(blood[i],patient[i])
    blood[i]-=minh
    patient[i]-=minh
    maxhelp+=minh

#neg across diff groups
#oneg
for i in range(2,8,2):
    if blood[0] != 0 and patient[i] != 0:
        minh = min(blood[0], patient[i])
        blood[0] -= minh
        patient[i] -= minh
        maxhelp += minh

#aneg,bneg help abneg
if blood[2] != 0 and patient[6] != 0:
    minh = min(blood[2], patient[6])
    blood[2] -= minh
    patient[6] -= minh
    maxhelp += minh
elif blood[4] != 0 and patient[6] != 0:
    minh = min(blood[4], patient[6])
    blood[4] -= minh
    patient[6] -= minh
    maxhelp += minh
elif blood[0] != 0 and patient[6] != 0:
    minh = min(blood[0], patient[6])
    blood[0] -= minh
    patient[6] -= minh
    maxhelp += minh

#positive across diff groups
#neg to pos in same group; o, a, b, ab
for i in range(0,8,2):
    if blood[i] != 0 and patient[i+1] != 0:
        minh = min(blood[i], patient[i+1])
        blood[i] -= minh
        patient[i+1] -= minh
        maxhelp += minh
#neg to pos in diff group
maxhelp += min(patient[7],blood[5]+blood[6])
maxhelp += min(patient[7],blood[4]+blood[3])
maxhelp += min(patient[5],blood[0]+blood[1])
maxhelp += min(patient[3],blood[0]+blood[1])
print(maxhelp)
