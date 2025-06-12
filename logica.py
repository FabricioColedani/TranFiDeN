# Tasas de conversión desde moneda extranjera a pesos argentinos
conversion_rates = {
    "Dólar": 1100,
    "Euro": 1170,
    "Libra": 1360,
    "Yen": 7.5
}

def convertir_moneda(monto_str, moneda_seleccionada):
    try:
        monto = float(monto_str)
        if moneda_seleccionada not in conversion_rates:
            raise ValueError("Moneda no válida")

        resultado = monto * conversion_rates[moneda_seleccionada]
        resultado_formateado = f"{monto} {moneda_seleccionada} = {resultado:,.2f} ARS Aprox." 
        return resultado_formateado, "#00B894"  # Éxito: texto y color
    except ValueError:
        return "Error: Ingrese un monto válido.", "#FF4D4D"  # Error: texto y color