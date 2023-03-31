# **** 1 ****
import data

def createCompanyBranches():
    
    companies = data.get_companies()
    branches = data.get_branches()
    
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

companies =  createCompanyBranches()

print(companies)




