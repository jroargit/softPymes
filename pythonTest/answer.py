import data

companies = data.get_companies()
branches = data.get_branches()

# **** 1 start ****

def createCompanyBranches(companies, branches):
    
    companies = companies
    branches = branches
    
    # Crear un diccionario vacío que contendrá las empresas y sus sucursales correspondientes
    company_branches = {}
    
    # Iterar sobre las empresas
    for company in companies:
        
        # Obtener las sucursales correspondientes a la empresa actual
        company_branch_ids = company['branches']
        company_branches_list = []
        for branch in branches:
            if branch['id'] in company_branch_ids:
                company_branches_list.append(branch)
        
        # Agregar la empresa y sus sucursales al diccionario
        company_branches[company['name']] = company_branches_list
        
    return company_branches

companiesFilter =  createCompanyBranches(companies, branches)

print(companiesFilter)

# **** 1 End ****

print("\n")

# **** 2 start ****
# to use this function have to set the id of the branch you want to see in id_sucursal
    
def getSucursalById(sucursales, id_sucursal):
    for sucursal in sucursales.values():
        for info_sucursal in sucursal:
            if info_sucursal['id'] == id_sucursal:
                return info_sucursal
    return None

id_sucursal = 5
info_sucursal = getSucursalById(companiesFilter, id_sucursal)

if info_sucursal:
    print(f"Información de la sucursal con id {id_sucursal}: {info_sucursal}")
else:
    print(f"No se encontró una sucursal con id {id_sucursal}")

# **** 2 end ****

print("\n")

# **** 3 start ****
thirds = data.get_thirds()

def getThirdName(thirds):
    thirdName = {}
    thirdNameList = []
    

    for data in thirds:
        if data["firstname"]!="":
            thirdNameList.append(data["firstname"], data["lastname"], data["maidenname"])
        else:
            thirdNameList.append(data["tradename"])

