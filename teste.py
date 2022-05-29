dias_trabalhados = float(input("Quantidade de dias trabalhados no mês: "))
funcionarios = int(input("Digite a quantidade de funcionários: "))
salario = float(input("digite o salário base: R$ "))
periculosidade = (salario/100*30)
vale_transporte = float(input("Digite o valor do Transporte da cidade: R$ "))
refeição = float(input("Digite o valor unitário do Vale refeição: R$ "))
cesta_basica = float(input("Digite o valor da cesta básica: R$ "))
seguro_vida = float(input("Digite o valor do seguro de vida: R$ "))
beneficio_social_familiar = float(input("Digite o valor do Beneficio Social Familiar: R$ "))
norma_regulamentadora = float(input("Digite o valor da Norma Rergulamentadora nº07: R$ "))
uniforme = float(input("Digite o valor do Uniforme: R$ "))
equipamentos = float(input("Digite o valor dos Equipamentos: R$ "))
reciclagem = float(input("Digite o valor da Reciclagem: R$ "))
encargos_sociais = float(input("Digite o Valor dos Encargos Sociais: "))
#INTRAJORNADA

# BDI
lucro = float(input("Digite a porcentagem de lucro: "))
administracao = float(input("Digite a porcentagem de administração: "))
issqn = float(input("Digite a porcentagem do ISS da cidade: "))
pis = float(input("Digite a porcentagem do PIS: "))
cofins = float(input("Digite a porcentagem do COFINS: "))

print("--*" * 20)

"""print("Dias trabalhados", dias_trabalhados)
print("O Salário base é R$", salario)
print("O Valor da Periculosidade: R$ ",periculosidade)
print("O Valor do Vale transporte unitário: R$ ", vale_transporte)
print("O Valor do Vale refeição: R$ ", refeição)
print("O Valor da Cesta Básica: R$ ", cesta_basica)
print("O Valor do Auxilio Funeral: R$ ",auxilio_funeral)
print("O Valor de Seguro de Vida: R$ ",seguro_vida)
print("O Valor do beneficio Social Familiar: R$ ", beneficio_social_familiar)
print("O Valor da Norma Regulamentadore nº7: R$ ", norma_regulamentadora)
print("O Valor do Uniforme: R$ ", uniforme)
print("O Valor dos Equipamentos: R$ ", equipamentos)
print("O Valor da Reciclagem: R$ ", reciclagem)
print("O Valor da Porcentagem é: ", encargos_sociais,"%")
print("O Valor do Lucro: ", lucro,"%")
print("O Valor da Administração: ", administracao,"%")
print("O Valor da ISSQN: ", issqn,"%")
print("O Valor da PIS: ", pis,"%")
print("O Valor da COFINS: ", cofins,"%")"""

print("--*" * 20)
#COMPOSIÇÃO SALARIAL
composicao_salarial = ((salario + periculosidade)*funcionarios)
print("Valor Total da Remuneração: R$",composicao_salarial)

#BENEFICIO DE VALE TRANSPORTE
print("--*" * 20)
transporte = ((vale_transporte * (dias_trabalhados*2))*funcionarios)
parcela_trab_vt = ((salario/100*6)*funcionarios)
transporte_total = (transporte - parcela_trab_vt)
transporte_total = round(transporte_total,2)
print("Valor Total do Vale Transporte: R$",transporte_total)

#BENEFICIO DE VALE REFEIÇÃO
print("--*" * 20)
vale_refeicao = ((refeição * dias_trabalhados)*funcionarios)
parcela_trab_vr = (vale_refeicao/100*18)
refeicao_total = (vale_refeicao-parcela_trab_vr)
refeicao_total = round(refeicao_total, 2)
print("Valor Total do Vale Refeição: R$",refeicao_total)

#BENEFICIO DE CESTA BÁSICA
print("--*" * 20)
cesta_basica_1 = ((cesta_basica)*funcionarios)
parcela_trab_cesta = ((cesta_basica/100*5)*funcionarios)
valor_total_cesta = (cesta_basica_1 - parcela_trab_cesta)
valor_total_cesta = round(valor_total_cesta,2)
print("Valor Total da Cesta Básica: R$",valor_total_cesta)

#AUXILIO FUNERAL
print("--*" * 20)
auxilio_funeral = ((((((salario*1.5)*(20/100))/12)*-9.25/100)+(((salario*1.5)*(20/100))/12))/100)*funcionarios
auxilio_funeral = round(auxilio_funeral,2)
print("Valor Total do Auxilio Funeral: R$",auxilio_funeral)

#SEGURO DE VIDA
print("--*" * 20)
seguro_vida_1 =( seguro_vida*funcionarios)
seguro_vida_1 = round(seguro_vida_1,2)
print("Valor Total do Seguro de Vida: R$",seguro_vida_1)

#BENEFICIO SOCIAL FAMILIAR
print("--*" * 20)
beneficio_social_familiar_1 = (beneficio_social_familiar*funcionarios)
parcela_trab_bsf = ((salario/100*7)*funcionarios)
total_bsf = (beneficio_social_familiar_1-parcela_trab_bsf)
total_bsf = round(total_bsf,2)
print("Valor Total do Beneficio Social Familiar: R$",total_bsf)

#NORMA REGULAMENTADORA Nº7
print("--*" * 20)
norma_regulamentadora_1 = (norma_regulamentadora*funcionarios)
norma_regulamentadora_1 = round(norma_regulamentadora_1,2)
print("Valor Total da Norma Regulamentadora nº7: R$",norma_regulamentadora_1)

"""INSUMOS DIVERSOS
UNIFORME
EQUIPAMENTOS
RECICLAGEM"""
print("--*" * 20)
insumos_diversos = ((uniforme + equipamentos + reciclagem)*funcionarios)
insumos_diversos = round(insumos_diversos,2)
print("Valor Total dos Insumos: R$",insumos_diversos)

#ENCARGOS SOCIAIS
print("--*" * 20)
encargos_sociais_trabalhistas = (composicao_salarial * (encargos_sociais/100))
encargos_sociais_trabalhistas = round(encargos_sociais_trabalhistas,2)
print("Valor Total dos Encargos Sociais: R$",encargos_sociais_trabalhistas)

#INTRAJORNADA
print("--*" * 20)
intrajornada = ((composicao_salarial + transporte_total + refeicao_total + valor_total_cesta + auxilio_funeral + seguro_vida_1 + total_bsf + norma_regulamentadora_1 + insumos_diversos + encargos_sociais_trabalhistas)/365.28)*30.44
intrajornada = round(intrajornada,2)
print("Valor Total da Intrajornada: R$",intrajornada)

#SUBTOTAL
print("--*" * 20)
subtotal = (composicao_salarial + transporte_total + refeicao_total + valor_total_cesta + auxilio_funeral + seguro_vida_1 + total_bsf + norma_regulamentadora_1 + insumos_diversos + encargos_sociais_trabalhistas + intrajornada)
subtotal = round(subtotal,2)
print("Valor SUBTOTAL: R$",subtotal)

#CUSTOS INDIRETOS
print("--*" * 20)
custos_indiretos = ((subtotal*(administracao/100)))
custos_indiretos = round(custos_indiretos,2)
print("O Valor do Custos Indiretos: R$ ",custos_indiretos)
lucro_1 = ((custos_indiretos+subtotal)*(lucro/100))
lucro_1 = round(lucro_1,2)
print("O valor do Lucro: R$ ",lucro_1)
total_lucro_administracao = (custos_indiretos + lucro_1)
total_lucro_administracao = round(total_lucro_administracao,2)
print("Valor do Lucro e Administração R$ ", total_lucro_administracao)

total_subtotal = subtotal + total_lucro_administracao
print("Subtotal e Lucros",total_subtotal )


#TRIBUTOS
print("--*" * 20)
total_posto = ((total_subtotal)/(100/100-((issqn/100)+(pis/100)+(cofins/100))))
total_posto = round(total_posto,2)
print("Valor Total do Posto: R$ ",total_posto)


iss_1 = (total_posto * (issqn/100))
iss_1 = round(iss_1,2)
print("Valor Total do ISS: R$ ",iss_1)

pis_1 = (total_posto * (pis/100))
pis_1 = round(pis_1,2)
print("Valor Total do PIS: R$ ",pis_1)

cofins_1 = (total_posto * (cofins/100))
cofins_1 = round(cofins_1,2)
print("Valor Total do COFINS: R$ ",cofins_1)


# TOTAL DE TRIBUTOS
total_tributos = (iss_1 + pis_1 + cofins_1)
total_tributos = round(total_tributos, 2)
print("TOTAL TRIBUTOS", total_tributos)

total_posto_1 = (total_subtotal + iss_1 + pis_1 + cofins_1)
total_posto_1 = round(total_posto_1,3)
print("Valor Total do POSTO: R$ ",total_posto_1)
