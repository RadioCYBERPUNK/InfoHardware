import subprocess

def get_hardware_info():
    try:
        # Informações da Memória RAM
        print("Informações da Memória RAM:")
        result = subprocess.check_output(["wmic", "memorychip", "get", "Manufacturer,Capacity,Speed,PartNumber,SerialNumber,DeviceLocator,ConfiguredClockSpeed,FormFactor,TypeDetail"])
        lines = result.decode("utf-8").split("\n")
        lines = lines[1:]
        for line in lines:
            info = line.strip().split()
            if len(info) >= 9:
                manufacturer = info[0]
                capacity = info[1]
                speed = info[2]
                model = info[3]
                serial_number = info[4]
                device_locator = info[5]
                configured_speed = info[6]
                form_factor = info[7]
                type_detail = info[8]
                
                print(f"Fabricante: {manufacturer}")
                print(f"Capacidade: {capacity} bytes")
                print(f"Velocidade: {speed} MHz")
                print(f"Modelo: {model}")
                print(f"Número de Série: {serial_number}")
                print(f"Localizador do Dispositivo: {device_locator}")
                print(f"Velocidade Configurada: {configured_speed} MHz")
                print(f"Form Factor: {form_factor}")
                print(f"Detalhes do Tipo: {type_detail}")
                print()
        
        # Informações do Processador (CPU)
        print("Informações do Processador (CPU):")
        result = subprocess.check_output(["wmic", "cpu", "get", "Name,MaxClockSpeed,NumberOfCores,NumberOfLogicalProcessors,Manufacturer"])
        lines = result.decode("utf-8").split("\n")
        lines = lines[1:]
        for line in lines:
            info = line.strip().split()
            if len(info) >= 5:
                name = info[0]
                max_clock_speed = info[1]
                num_cores = info[2]
                num_logical_processors = info[3]
                manufacturer = info[4]
                
                print(f"Nome: {name}")
                print(f"Velocidade Máxima do Clock: {max_clock_speed} MHz")
                print(f"Número de Cores: {num_cores}")
                print(f"Número de Processadores Lógicos: {num_logical_processors}")
                print(f"Fabricante: {manufacturer}")
                print()
        
        # Informações da Placa-Mãe
        print("Informações da Placa-Mãe:")
        result = subprocess.check_output(["wmic", "baseboard", "get", "Product,Manufacturer,SerialNumber,Version"])
        lines = result.decode("utf-8").split("\n")
        lines = lines[1:]
        for line in lines:
            info = line.strip().split()
            if len(info) >= 4:
                product = info[0]
                manufacturer = info[1]
                serial_number = info[2]
                version = info[3]
                
                print(f"Produto: {product}")
                print(f"Fabricante: {manufacturer}")
                print(f"Número de Série: {serial_number}")
                print(f"Versão: {version}")
                print()
        
        # Informações dos Discos Rígidos
        print("Informações dos Discos Rígidos:")
        result = subprocess.check_output(["wmic", "diskdrive", "get", "Model,Size,MediaType"])
        lines = result.decode("utf-8").split("\n")
        lines = lines[1:]
        for line in lines:
            info = line.strip().split()
            if len(info) >= 3:
                model = info[0]
                size = info[1]
                media_type = info[2]
                
                print(f"Modelo: {model}")
                print(f"Tamanho: {size} bytes")
                print(f"Tipo de Mídia: {media_type}")
                print()
        

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    get_hardware_info()
