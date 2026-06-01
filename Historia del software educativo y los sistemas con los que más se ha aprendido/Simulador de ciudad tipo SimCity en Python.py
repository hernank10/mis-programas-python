import random
import math
import sys
import time
import json
from enum import Enum
from collections import defaultdict
from datetime import datetime, timedelta
import os

class ZoneType(Enum):
    """Tipos de zonas en la ciudad"""
    EMPTY = " "
    RESIDENTIAL = "R"
    COMMERCIAL = "C"
    INDUSTRIAL = "I"
    ROAD = "═"
    POWER_PLANT = "P"
    WATER_PLANT = "W"
    POLICE = "⚖"
    FIRE = "🚒"
    HOSPITAL = "🏥"
    SCHOOL = "🏫"
    PARK = "🌳"
    POWER_LINE = "▬"

class BuildingLevel(Enum):
    """Niveles de desarrollo de edificios"""
    VACANT = 0
    LOW_DENSITY = 1
    MEDIUM_DENSITY = 2
    HIGH_DENSITY = 3

class DisasterType(Enum):
    """Tipos de desastres naturales"""
    NONE = 0
    FIRE = 1
    FLOOD = 2
    EARTHQUAKE = 3
    TORNADO = 4
    RIOT = 5

class SimCity:
    """
    Simulador de ciudad tipo SimCity en Python
    Enseña urbanismo, gestión de recursos y pensamiento sistémico
    """
    
    def __init__(self, city_name="Nueva Ciudad", width=20, height=15):
        # Configuración básica
        self.city_name = city_name
        self.width = width
        self.height = height
        self.year = 2024
        self.month = 1
        self.day = 1
        self.total_days = 0
        
        # Estado financiero
        self.budget = 1000000  # Presupuesto inicial
        self.tax_rate = 0.10   # Tasa de impuestos (10%)
        self.income = 0
        self.expenses = 0
        self.debt = 0
        
        # Estadísticas de la ciudad
        self.population = 0
        self.residential_population = 0
        self.commercial_population = 0
        self.industrial_population = 0
        self.employment_rate = 0.0
        self.happiness = 75  # 0-100
        self.pollution = 0   # 0-100
        self.crime_rate = 5  # 0-100
        self.education_level = 50  # 0-100
        self.health_level = 70     # 0-100
        
        # Recursos y servicios
        self.power_supply = 0
        self.power_demand = 0
        self.water_supply = 0
        self.water_demand = 0
        self.police_coverage = 0   # Porcentaje
        self.fire_coverage = 0     # Porcentaje
        self.hospital_capacity = 0 # Personas
        self.school_capacity = 0   # Estudiantes
        
        # Mapa de la ciudad
        self.grid = []
        self.building_levels = []
        self.power_grid = []
        self.water_grid = []
        self.initialize_grid()
        
        # Registros históricos
        self.history = {
            'population': [],
            'budget': [],
            'happiness': [],
            'events': []
        }
        
        # Eventos y desastres
        self.active_disasters = []
        self.events = []
        
        # Precios de construcción
        self.construction_costs = {
            ZoneType.RESIDENTIAL: 1000,
            ZoneType.COMMERCIAL: 1500,
            ZoneType.INDUSTRIAL: 2000,
            ZoneType.ROAD: 100,
            ZoneType.POWER_PLANT: 50000,
            ZoneType.WATER_PLANT: 30000,
            ZoneType.POLICE: 20000,
            ZoneType.FIRE: 15000,
            ZoneType.HOSPITAL: 75000,
            ZoneType.SCHOOL: 40000,
            ZoneType.PARK: 5000,
            ZoneType.POWER_LINE: 50
        }
        
        # Costos de mantenimiento mensual
        self.maintenance_costs = {
            ZoneType.RESIDENTIAL: 10,
            ZoneType.COMMERCIAL: 15,
            ZoneType.INDUSTRIAL: 20,
            ZoneType.ROAD: 5,
            ZoneType.POWER_PLANT: 1000,
            ZoneType.WATER_PLANT: 800,
            ZoneType.POLICE: 500,
            ZoneType.FIRE: 400,
            ZoneType.HOSPITAL: 1500,
            ZoneType.SCHOOL: 800,
            ZoneType.PARK: 100,
            ZoneType.POWER_LINE: 2
        }
        
        # Salarios por tipo de zona
        self.salaries = {
            ZoneType.RESIDENTIAL: 0,
            ZoneType.COMMERCIAL: 50000,
            ZoneType.INDUSTRIAL: 40000
        }
        
        # Consumos
        self.power_consumption = {
            ZoneType.RESIDENTIAL: 2,
            ZoneType.COMMERCIAL: 3,
            ZoneType.INDUSTRIAL: 5,
            ZoneType.POLICE: 10,
            ZoneType.FIRE: 10,
            ZoneType.HOSPITAL: 20,
            ZoneType.SCHOOL: 15,
            ZoneType.POWER_PLANT: 0,
            ZoneType.WATER_PLANT: 15
        }
        
        self.water_consumption = {
            ZoneType.RESIDENTIAL: 1,
            ZoneType.COMMERCIAL: 2,
            ZoneType.INDUSTRIAL: 3,
            ZoneType.POLICE: 5,
            ZoneType.FIRE: 5,
            ZoneType.HOSPITAL: 10,
            ZoneType.SCHOOL: 8,
            ZoneType.POWER_PLANT: 5,
            ZoneType.WATER_PLANT: 0
        }
        
        # Tasa de crecimiento
        self.growth_factors = {
            'residential': 1.0,
            'commercial': 1.0,
            'industrial': 1.0
        }
        
        # Inicializar sistema de juego
        self.game_over = False
        self.message_log = []
        self.last_calculation = None
        
        print(f"\n🏙️  Fundando {self.city_name}...")
        print("💰 Presupuesto inicial: ${:,}".format(self.budget))
        time.sleep(2)
    
    def initialize_grid(self):
        """Inicializa el mapa de la ciudad"""
        self.grid = []
        self.building_levels = []
        self.power_grid = []
        self.water_grid = []
        
        for y in range(self.height):
            row = []
            level_row = []
            power_row = []
            water_row = []
            
            for x in range(self.width):
                # Crear un poco de terreno aleatorio
                if random.random() < 0.1:
                    row.append("≈")  # Agua
                else:
                    row.append(ZoneType.EMPTY.value)
                
                level_row.append(BuildingLevel.VACANT)
                power_row.append(False)
                water_row.append(False)
            
            self.grid.append(row)
            self.building_levels.append(level_row)
            self.power_grid.append(power_row)
            self.water_grid.append(water_row)
    
    def clear_screen(self):
        """Limpia la pantalla de la consola"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_city(self):
        """Muestra el mapa de la ciudad"""
        self.clear_screen()
        
        # Encabezado
        print("═" * 80)
        print(f"🏙️  {self.city_name} - Año: {self.year} - Mes: {self.month}")
        print(f"👥 Población: {self.population:,} | 💰 Presupuesto: ${self.budget:,}")
        print(f"😊 Felicidad: {self.happiness}% | 🏭 Contaminación: {self.pollution}%")
        print("═" * 80)
        
        # Leyenda
        print("\nLEYENDA:")
        print("R = Residencial | C = Comercial | I = Industrial | ═ = Carretera")
        print("P = Planta Energía | W = Planta Agua | ⚖ = Policía | 🚒 = Bomberos")
        print("🏥 = Hospital | 🏫 = Escuela | 🌳 = Parque | ▬ = Línea Eléctrica")
        print("≈ = Agua | ■ = Edificio desarrollado")
        print("-" * 80)
        
        # Mostrar coordenadas en X
        print("   " + "".join([f"{i:2}" for i in range(self.width)]))
        
        # Mostrar mapa
        for y in range(self.height):
            # Coordenada Y
            print(f"{y:2} ", end="")
            
            for x in range(self.width):
                cell = self.grid[y][x]
                level = self.building_levels[y][x]
                
                # Mostrar con color según tipo
                if cell == ZoneType.EMPTY.value:
                    print("· ", end="")
                elif cell == ZoneType.RESIDENTIAL.value:
                    if level == BuildingLevel.HIGH_DENSITY:
                        print("▓ ", end="")
                    elif level == BuildingLevel.MEDIUM_DENSITY:
                        print("▒ ", end="")
                    elif level == BuildingLevel.LOW_DENSITY:
                        print("░ ", end="")
                    else:
                        print("R ", end="")
                elif cell == ZoneType.COMMERCIAL.value:
                    if level == BuildingLevel.HIGH_DENSITY:
                        print("▓ ", end="")
                    elif level == BuildingLevel.MEDIUM_DENSITY:
                        print("▒ ", end="")
                    else:
                        print("C ", end="")
                elif cell == ZoneType.INDUSTRIAL.value:
                    print("I ", end="")
                elif cell == "≈":
                    print("≈ ", end="")
                else:
                    print(f"{cell} ", end="")
            
            print()
        
        print("\n" + "═" * 80)
    
    def display_stats(self):
        """Muestra estadísticas detalladas de la ciudad"""
        print("\n📊 ESTADÍSTICAS DETALLADAS:")
        print(f"   👥 Población total: {self.population:,}")
        print(f"   🏠 Residencial: {self.residential_population:,}")
        print(f"   🛒 Comercial: {self.commercial_population:,}")
        print(f"   🏭 Industrial: {self.industrial_population:,}")
        
        print(f"\n   💼 Tasa de empleo: {self.employment_rate:.1f}%")
        print(f"   💰 Tasa de impuestos: {self.tax_rate*100:.1f}%")
        print(f"   📈 Ingresos mensuales: ${self.income:,}")
        print(f"   📉 Gastos mensuales: ${self.expenses:,}")
        
        print(f"\n   ⚡ Energía: {self.power_supply:,}/{self.power_demand:,}")
        power_status = "✅ Suficiente" if self.power_supply >= self.power_demand else "❌ Insuficiente"
        print(f"     Estado: {power_status}")
        
        print(f"   💧 Agua: {self.water_supply:,}/{self.water_demand:,}")
        water_status = "✅ Suficiente" if self.water_supply >= self.water_demand else "❌ Insuficiente"
        print(f"     Estado: {water_status}")
        
        print(f"\n   👮 Cobertura policial: {self.police_coverage:.1f}%")
        print(f"   🚒 Cobertura de bomberos: {self.fire_coverage:.1f}%")
        print(f"   🏥 Capacidad hospitalaria: {self.hospital_capacity:,}")
        print(f"   🏫 Capacidad escolar: {self.school_capacity:,}")
        
        print(f"\n   📚 Nivel educativo: {self.education_level}/100")
        print(f"   🩺 Nivel de salud: {self.health_level}/100")
        print(f"   ⚖️  Tasa de criminalidad: {self.crime_rate}/100")
        
        # Factores de crecimiento
        print(f"\n   📈 Factores de crecimiento:")
        for zone_type, factor in self.growth_factors.items():
            status = "📈" if factor > 1.0 else "📉" if factor < 1.0 else "➡️"
            print(f"     {zone_type.capitalize()}: {factor:.2f} {status}")
    
    def display_menu(self):
        """Muestra el menú principal"""
        print("\n🎮 MENÚ PRINCIPAL:")
        print("1. 🔨 Construir")
        print("2. 🗑️  Demoler")
        print("3. 🔍 Ver estadísticas")
        print("4. ⚙️  Configurar impuestos")
        print("5. ⏩ Avanzar 1 mes")
        print("6. ⏭️  Avanzar 1 año")
        print("7. 💾 Guardar ciudad")
        print("8. 📂 Cargar ciudad")
        print("9. 🏆 Logros y objetivos")
        print("0. 🚪 Salir del juego")
        
        print("\n📝 Últimos mensajes:")
        for msg in self.message_log[-3:]:
            print(f"   {msg}")
        
        return input("\n👉 Selecciona una opción: ").strip()
    
    def build_menu(self):
        """Muestra el menú de construcción"""
        print("\n🔨 MENÚ DE CONSTRUCCIÓN:")
        print("1. 🏠 Zona Residencial - ${:,}".format(self.construction_costs[ZoneType.RESIDENTIAL]))
        print("2. 🛒 Zona Comercial - ${:,}".format(self.construction_costs[ZoneType.COMMERCIAL]))
        print("3. 🏭 Zona Industrial - ${:,}".format(self.construction_costs[ZoneType.INDUSTRIAL]))
        print("4. 🛣️  Carretera - ${:,}".format(self.construction_costs[ZoneType.ROAD]))
        print("5. ⚡ Planta de Energía - ${:,}".format(self.construction_costs[ZoneType.POWER_PLANT]))
        print("6. 💧 Planta de Agua - ${:,}".format(self.construction_costs[ZoneType.WATER_PLANT]))
        print("7. 👮 Estación de Policía - ${:,}".format(self.construction_costs[ZoneType.POLICE]))
        print("8. 🚒 Estación de Bomberos - ${:,}".format(self.construction_costs[ZoneType.FIRE]))
        print("9. 🏥 Hospital - ${:,}".format(self.construction_costs[ZoneType.HOSPITAL]))
        print("10. 🏫 Escuela - ${:,}".format(self.construction_costs[ZoneType.SCHOOL]))
        print("11. 🌳 Parque - ${:,}".format(self.construction_costs[ZoneType.PARK]))
        print("12. 🔌 Línea Eléctrica - ${:,}".format(self.construction_costs[ZoneType.POWER_LINE]))
        print("0. ↩️  Volver al menú principal")
        
        return input("\n👉 Selecciona lo que quieres construir: ").strip()
    
    def build(self, zone_type, x, y):
        """Construye en una coordenada específica"""
        if not self.is_valid_position(x, y):
            self.add_message("❌ Posición inválida")
            return False
        
        # Verificar si ya hay algo construido
        if self.grid[y][x] != ZoneType.EMPTY.value and self.grid[y][x] != "≈":
            self.add_message("❌ Ya hay algo construido aquí")
            return False
        
        # Verificar costo
        cost = self.construction_costs.get(zone_type, 0)
        if cost > self.budget:
            self.add_message(f"❌ No tienes suficiente dinero (necesitas ${cost:,})")
            return False
        
        # Construir
        self.grid[y][x] = zone_type.value
        self.budget -= cost
        self.add_message(f"✅ Construido {zone_type.name} en ({x},{y}) por ${cost:,}")
        
        # Si es una planta de energía o agua, generar recursos
        if zone_type == ZoneType.POWER_PLANT:
            self.power_supply += 1000
        elif zone_type == ZoneType.WATER_PLANT:
            self.water_supply += 1000
        
        # Si es una línea eléctrica, actualizar red eléctrica
        if zone_type == ZoneType.POWER_LINE:
            self.update_power_grid(x, y)
        
        return True
    
    def demolish(self, x, y):
        """Demuele una construcción"""
        if not self.is_valid_position(x, y):
            self.add_message("❌ Posición inválida")
            return False
        
        # Verificar si hay algo para demoler
        if self.grid[y][x] == ZoneType.EMPTY.value or self.grid[y][x] == "≈":
            self.add_message("❌ No hay nada para demoler aquí")
            return False
        
        # Obtener tipo de construcción
        current_value = self.grid[y][x]
        
        # Encontrar el tipo de zona
        zone_type = None
        for zt in ZoneType:
            if zt.value == current_value:
                zone_type = zt
                break
        
        # Demoler (devolver parte del costo)
        if zone_type:
            refund = self.construction_costs.get(zone_type, 0) * 0.25  # 25% de reembolso
            self.budget += int(refund)
            self.add_message(f"🗑️  Demolido {zone_type.name} en ({x},{y}), reembolso: ${int(refund):,}")
        else:
            self.add_message(f"🗑️  Demolido construcción en ({x},{y})")
        
        # Restablecer a vacío
        self.grid[y][x] = ZoneType.EMPTY.value
        self.building_levels[y][x] = BuildingLevel.VACANT
        
        return True
    
    def is_valid_position(self, x, y):
        """Verifica si una posición es válida en el mapa"""
        return 0 <= x < self.width and 0 <= y < self.height
    
    def update_power_grid(self, start_x, start_y):
        """Actualiza la red eléctrica desde una posición"""
        # BFS para propagar energía
        visited = [[False for _ in range(self.width)] for _ in range(self.height)]
        queue = [(start_x, start_y)]
        
        while queue:
            x, y = queue.pop(0)
            
            if not self.is_valid_position(x, y) or visited[y][x]:
                continue
            
            visited[y][x] = True
            self.power_grid[y][x] = True
            
            # Agregar vecinos si tienen conexión
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx, ny = x + dx, y + dy
                if self.is_valid_position(nx, ny):
                    # Solo agregar si es una construcción que puede tener energía
                    neighbor_cell = self.grid[ny][nx]
                    if (neighbor_cell != ZoneType.EMPTY.value and 
                        neighbor_cell != "≈" and
                        neighbor_cell != ZoneType.POWER_LINE.value):
                        queue.append((nx, ny))
    
    def calculate_monthly_updates(self):
        """Calcula las actualizaciones mensuales de la ciudad"""
        self.last_calculation = {
            'income': 0,
            'expenses': 0,
            'population_change': 0,
            'happiness_change': 0
        }
        
        # Calcular población por zonas
        self.calculate_population()
        
        # Calcular demanda de servicios
        self.calculate_demand()
        
        # Calcular ingresos por impuestos
        self.calculate_income()
        
        # Calcular gastos por mantenimiento
        self.calculate_expenses()
        
        # Calcular factores de crecimiento
        self.calculate_growth_factors()
        
        # Actualizar estadísticas
        self.update_statistics()
        
        # Generar eventos aleatorios
        self.generate_random_events()
        
        # Actualizar fecha
        self.advance_time()
        
        # Agregar a historial
        self.record_history()
        
        # Verificar condiciones de fin de juego
        self.check_game_over()
    
    def calculate_population(self):
        """Calcula la población basada en las zonas residenciales"""
        residential_count = 0
        commercial_count = 0
        industrial_count = 0
        
        for y in range(self.height):
            for x in range(self.width):
                cell = self.grid[y][x]
                level = self.building_levels[y][x]
                
                if cell == ZoneType.RESIDENTIAL.value:
                    # Población por nivel de edificio
                    if level == BuildingLevel.LOW_DENSITY:
                        residential_count += 10
                    elif level == BuildingLevel.MEDIUM_DENSITY:
                        residential_count += 25
                    elif level == BuildingLevel.HIGH_DENSITY:
                        residential_count += 50
                    else:
                        residential_count += 5
                
                elif cell == ZoneType.COMMERCIAL.value:
                    # Empleos comerciales
                    if level == BuildingLevel.LOW_DENSITY:
                        commercial_count += 5
                    elif level == BuildingLevel.MEDIUM_DENSITY:
                        commercial_count += 15
                    elif level == BuildingLevel.HIGH_DENSITY:
                        commercial_count += 30
                    else:
                        commercial_count += 3
                
                elif cell == ZoneType.INDUSTRIAL.value:
                    # Empleos industriales
                    industrial_count += 20
        
        self.residential_population = residential_count
        self.commercial_population = commercial_count
        self.industrial_population = industrial_count
        
        # Población total
        old_population = self.population
        self.population = residential_count
        
        # Tasa de empleo
        total_jobs = commercial_count + industrial_count
        if self.population > 0:
            self.employment_rate = min(100, (total_jobs / self.population) * 100)
        
        # Cambio en población
        pop_change = self.population - old_population
        if pop_change > 0:
            self.add_message(f"📈 Población aumentó en {pop_change:,}")
        elif pop_change < 0:
            self.add_message(f"📉 Población disminuyó en {abs(pop_change):,}")
    
    def calculate_demand(self):
        """Calcula la demanda de energía, agua y otros servicios"""
        self.power_demand = 0
        self.water_demand = 0
        
        # Contar servicios
        police_stations = 0
        fire_stations = 0
        hospitals = 0
        schools = 0
        parks = 0
        
        for y in range(self.height):
            for x in range(self.width):
                cell = self.grid[y][x]
                
                # Calcular consumo
                for zone_type, consumption in self.power_consumption.items():
                    if zone_type.value == cell:
                        self.power_demand += consumption
                
                for zone_type, consumption in self.water_consumption.items():
                    if zone_type.value == cell:
                        self.water_demand += consumption
                
                # Contar servicios
                if cell == ZoneType.POLICE.value:
                    police_stations += 1
                elif cell == ZoneType.FIRE.value:
                    fire_stations += 1
                elif cell == ZoneType.HOSPITAL.value:
                    hospitals += 1
                elif cell == ZoneType.SCHOOL.value:
                    schools += 1
                elif cell == ZoneType.PARK.value:
                    parks += 1
        
        # Calcular cobertura de servicios
        total_area = self.width * self.height
        
        # Cobertura policial y de bomberos
        service_coverage = 0
        if police_stations > 0:
            service_coverage = min(100, (police_stations * 20))
        self.police_coverage = service_coverage
        
        service_coverage = 0
        if fire_stations > 0:
            service_coverage = min(100, (fire_stations * 20))
        self.fire_coverage = service_coverage
        
        # Capacidad hospitalaria y escolar
        self.hospital_capacity = hospitals * 1000
        self.school_capacity = schools * 500
        
        # Efecto de parques en felicidad
        park_effect = min(10, parks * 2)
        
        # Actualizar felicidad basada en servicios
        service_happiness = 0
        if self.police_coverage > 50:
            service_happiness += 5
        if self.fire_coverage > 50:
            service_happiness += 5
        if self.hospital_capacity > self.population / 10:
            service_happiness += 5
        if self.school_capacity > self.population / 5:
            service_happiness += 5
        
        self.happiness = min(100, max(0, self.happiness + service_happiness + park_effect))
    
    def calculate_income(self):
        """Calcula los ingresos mensuales"""
        # Ingresos por impuestos
        tax_income = 0
        
        # Ingresos residenciales
        residential_income = self.residential_population * self.tax_rate * 100
        tax_income += residential_income
        
        # Ingresos comerciales e industriales
        commercial_income = self.commercial_population * self.tax_rate * 500
        industrial_income = self.industrial_population * self.tax_rate * 400
        
        tax_income += commercial_income + industrial_income
        
        self.income = int(tax_income)
        self.budget += self.income
        
        self.last_calculation['income'] = self.income
    
    def calculate_expenses(self):
        """Calcula los gastos mensuales"""
        monthly_expenses = 0
        
        # Calcular gastos de mantenimiento
        for y in range(self.height):
            for x in range(self.width):
                cell = self.grid[y][x]
                
                for zone_type, cost in self.maintenance_costs.items():
                    if zone_type.value == cell:
                        monthly_expenses += cost
        
        # Gastos por deuda
        if self.debt > 0:
            interest = self.debt * 0.05  # 5% de interés
            monthly_expenses += interest
        
        self.expenses = int(monthly_expenses)
        self.budget -= self.expenses
        
        self.last_calculation['expenses'] = self.expenses
        
        # Verificar si hay déficit
        if self.expenses > self.income:
            deficit = self.expenses - self.income
            self.add_message(f"⚠️  Déficit mensual de ${deficit:,}")
    
    def calculate_growth_factors(self):
        """Calcula los factores de crecimiento para cada tipo de zona"""
        # Factor base
        base_growth = 1.0
        
        # Modificadores por felicidad
        happiness_modifier = self.happiness / 100
        
        # Modificadores por servicios
        service_modifier = 1.0
        
        if self.power_supply < self.power_demand:
            service_modifier *= 0.8
            self.add_message("⚠️  Apagones están afectando el crecimiento")
        
        if self.water_supply < self.water_demand:
            service_modifier *= 0.8
            self.add_message("⚠️  Escasez de agua está afectando el crecimiento")
        
        if self.employment_rate < 80:
            service_modifier *= 0.9
        
        if self.crime_rate > 30:
            service_modifier *= 0.7
        
        # Aplicar modificadores
        growth_factor = base_growth * happiness_modifier * service_modifier
        
        # Factores específicos por zona
        self.growth_factors['residential'] = growth_factor
        self.growth_factors['commercial'] = growth_factor * (self.residential_population / max(1, self.population))
        self.growth_factors['industrial'] = growth_factor * (self.commercial_population / max(1, self.population))
    
    def update_statistics(self):
        """Actualiza las estadísticas de la ciudad"""
        # Actualizar contaminación
        pollution_from_industrial = self.industrial_population * 0.1
        pollution_from_power = 0
        
        if self.power_supply > 0:
            power_plants = sum(1 for row in self.grid for cell in row if cell == ZoneType.POWER_PLANT.value)
            pollution_from_power = power_plants * 5
        
        # Reducción por parques
        parks = sum(1 for row in self.grid for cell in row if cell == ZoneType.PARK.value)
        pollution_reduction = parks * 2
        
        self.pollution = min(100, max(0, 
            self.pollution + pollution_from_industrial + pollution_from_power - pollution_reduction
        ))
        
        # Actualizar criminalidad
        crime_base = 5
        crime_from_population = self.population / 10000
        crime_reduction = (self.police_coverage / 100) * 20
        crime_from_unemployment = 0
        
        if self.employment_rate < 80:
            crime_from_unemployment = (80 - self.employment_rate) / 10
        
        self.crime_rate = min(100, max(0,
            crime_base + crime_from_population + crime_from_unemployment - crime_reduction
        ))
        
        # Actualizar educación
        education_base = 50
        education_from_schools = (self.school_capacity / max(1, self.population)) * 30
        self.education_level = min(100, education_base + education_from_schools)
        
        # Actualizar salud
        health_base = 70
        health_from_hospitals = (self.hospital_capacity / max(1, self.population)) * 20
        health_from_pollution = -self.pollution * 0.2
        self.health_level = min(100, max(0,
            health_base + health_from_hospitals + health_from_pollution
        ))
        
        # Actualizar niveles de edificios
        self.update_building_levels()
    
    def update_building_levels(self):
        """Actualiza los niveles de desarrollo de los edificios"""
        for y in range(self.height):
            for x in range(self.width):
                cell = self.grid[y][x]
                current_level = self.building_levels[y][x]
                
                # Solo actualizar zonas residenciales y comerciales
                if cell in [ZoneType.RESIDENTIAL.value, ZoneType.COMMERCIAL.value]:
                    
                    # Determinar factor de crecimiento
                    growth_factor = 1.0
                    if cell == ZoneType.RESIDENTIAL.value:
                        growth_factor = self.growth_factors['residential']
                    elif cell == ZoneType.COMMERCIAL.value:
                        growth_factor = self.growth_factors['commercial']
                    
                    # Determinar si el edificio puede crecer
                    if growth_factor > 1.2 and current_level.value < BuildingLevel.HIGH_DENSITY.value:
                        # Crecer
                        new_level_value = min(
                            BuildingLevel.HIGH_DENSITY.value,
                            current_level.value + 1
                        )
                        self.building_levels[y][x] = BuildingLevel(new_level_value)
                        
                        if new_level_value > current_level.value:
                            self.add_message(f"🏗️  Edificio en ({x},{y}) ha crecido a nivel {new_level_value}")
                    
                    elif growth_factor < 0.8 and current_level.value > BuildingLevel.VACANT.value:
                        # Disminuir
                        new_level_value = max(
                            BuildingLevel.VACANT.value,
                            current_level.value - 1
                        )
                        self.building_levels[y][x] = BuildingLevel(new_level_value)
                        
                        if new_level_value < current_level.value:
                            self.add_message(f"⚠️  Edificio en ({x},{y}) ha disminuido a nivel {new_level_value}")
    
    def advance_time(self):
        """Avanza el tiempo en la simulación"""
        self.month += 1
        self.total_days += 30
        
        if self.month > 12:
            self.month = 1
            self.year += 1
            self.add_message(f"🎉 ¡Año nuevo! {self.year}")
    
    def generate_random_events(self):
        """Genera eventos aleatorios que afectan la ciudad"""
        event_chance = 0.2  # 20% de chance cada mes
        
        if random.random() < event_chance:
            events = [
                ("🎉 Festival de la ciudad", "La felicidad aumenta temporalmente", 10),
                ("🦠 Brote de enfermedad", "La salud pública disminuye", -15),
                ("🎓 Graduación masiva", "El nivel educativo aumenta", 5),
                ("💸 Boom económico", "Los ingresos aumentan este mes", 20),
                ("🌧️  Lluvias torrenciales", "Algunas zonas se inundan", -10),
                ("🏆 Premio a la ciudad más verde", "Reconocimiento internacional", 5)
            ]
            
            event, description, effect = random.choice(events)
            
            # Aplicar efecto
            if "felicidad" in description.lower():
                self.happiness = min(100, self.happiness + effect)
            elif "salud" in description.lower():
                self.health_level = max(0, self.health_level + effect)
            elif "educativo" in description.lower():
                self.education_level = min(100, self.education_level + effect)
            elif "ingresos" in description.lower():
                bonus = self.income * (effect / 100)
                self.budget += int(bonus)
                self.add_message(f"💰 Bono económico: ${int(bonus):,}")
            
            self.add_message(f"📰 Evento: {event} - {description}")
            self.events.append((self.year, self.month, event, description))
    
    def record_history(self):
        """Registra el estado actual en el historial"""
        self.history['population'].append(self.population)
        self.history['budget'].append(self.budget)
        self.history['happiness'].append(self.happiness)
    
    def check_game_over(self):
        """Verifica condiciones de fin de juego"""
        # Si la ciudad está en bancarrota por mucho tiempo
        if self.budget < -1000000:
            self.game_over = True
            self.add_message("💸 ¡BANCARROTA! La ciudad ha quebrado.")
        
        # Si la felicidad es muy baja por mucho tiempo
        if self.happiness < 10 and self.population > 100:
            self.game_over = True
            self.add_message("😡 ¡REVOLUCIÓN! Los ciudadanos se han rebelado.")
        
        # Si la población cae a 0
        if self.population == 0:
            self.game_over = True
            self.add_message("👻 ¡CIUDAD FANTASMA! Todos se han ido.")
    
    def set_tax_rate(self):
        """Permite al jugador ajustar la tasa de impuestos"""
        print(f"\n💰 Tasa de impuestos actual: {self.tax_rate*100:.1f}%")
        print("⚠️  Tasas muy altas reducen la felicidad, tasas muy bajas reducen ingresos")
        
        try:
            new_rate = float(input("Nueva tasa de impuestos (0-50%): ").strip())
            new_rate = max(0, min(50, new_rate)) / 100
            
            if new_rate != self.tax_rate:
                self.tax_rate = new_rate
                self.add_message(f"📊 Tasa de impuestos ajustada a {new_rate*100:.1f}%")
                
                # Efecto en felicidad
                happiness_change = (self.tax_rate - 0.1) * -100  # 10% es óptimo
                self.happiness = max(0, min(100, self.happiness + happiness_change))
        except ValueError:
            self.add_message("❌ Valor no válido")
    
    def add_message(self, message):
        """Agrega un mensaje al registro"""
        timestamp = f"[{self.year}-{self.month:02d}]"
        self.message_log.append(f"{timestamp} {message}")
        
        # Mantener solo los últimos 10 mensajes
        if len(self.message_log) > 10:
            self.message_log = self.message_log[-10:]
    
    def show_achievements(self):
        """Muestra logros y objetivos"""
        print("\n🏆 LOGROS Y OBJETIVOS:")
        print("=" * 60)
        
        achievements = [
            ("🏙️  Ciudad pequeña", "Alcanza 1,000 habitantes", self.population >= 1000),
            ("💰 Millonario", "Alcanza $1,000,000 en presupuesto", self.budget >= 1000000),
            ("😊 Ciudad feliz", "Mantén felicidad > 80% por 12 meses", self.happiness > 80),
            ("🌿 Ciudad verde", "Mantén contaminación < 20%", self.pollution < 20),
            ("🎓 Ciudad educada", "Alcanza nivel educativo > 80", self.education_level > 80),
            ("👮 Ciudad segura", "Mantén criminalidad < 10%", self.crime_rate < 10),
        ]
        
        completed = 0
        for name, description, achieved in achievements:
            status = "✅" if achieved else "⏳"
            if achieved:
                completed += 1
            print(f"{status} {name}: {description}")
        
        print(f"\n📊 Progreso: {completed}/{len(achievements)} logros completados")
        
        # Objetivos sugeridos
        print("\n🎯 OBJETIVOS SUGERIDOS:")
        if self.power_demand > self.power_supply:
            print("🔧 Construye más plantas de energía")
        if self.water_demand > self.water_supply:
            print("🔧 Construye más plantas de agua")
        if self.crime_rate > 20:
            print("🔧 Construye más estaciones de policía")
        if self.employment_rate < 80:
            print("🔧 Construye más zonas comerciales e industriales")
        if self.happiness < 60:
            print("🔧 Construye parques y mejora servicios")
        
        input("\n⏎ Presiona Enter para continuar...")
    
    def save_city(self):
        """Guarda el estado de la ciudad en un archivo"""
        filename = f"{self.city_name.replace(' ', '_')}.json"
        
        save_data = {
            'city_name': self.city_name,
            'width': self.width,
            'height': self.height,
            'year': self.year,
            'month': self.month,
            'total_days': self.total_days,
            'budget': self.budget,
            'tax_rate': self.tax_rate,
            'population': self.population,
            'happiness': self.happiness,
            'pollution': self.pollution,
            'crime_rate': self.crime_rate,
            'education_level': self.education_level,
            'health_level': self.health_level,
            'grid': self.grid,
            'building_levels': [[level.value for level in row] for row in self.building_levels],
            'history': self.history,
            'events': self.events
        }
        
        try:
            with open(filename, 'w') as f:
                json.dump(save_data, f, indent=2)
            
            self.add_message(f"💾 Ciudad guardada en '{filename}'")
            return True
        except Exception as e:
            self.add_message(f"❌ Error al guardar: {str(e)}")
            return False
    
    def load_city(self):
        """Carga una ciudad desde un archivo"""
        filename = input("Nombre del archivo a cargar (sin .json): ").strip()
        if not filename:
            return False
        
        filename = f"{filename}.json"
        
        try:
            with open(filename, 'r') as f:
                save_data = json.load(f)
            
            # Cargar datos básicos
            self.city_name = save_data['city_name']
            self.width = save_data['width']
            self.height = save_data['height']
            self.year = save_data['year']
            self.month = save_data['month']
            self.total_days = save_data['total_days']
            self.budget = save_data['budget']
            self.tax_rate = save_data['tax_rate']
            self.population = save_data['population']
            self.happiness = save_data['happiness']
            self.pollution = save_data['pollution']
            self.crime_rate = save_data['crime_rate']
            self.education_level = save_data['education_level']
            self.health_level = save_data['health_level']
            self.grid = save_data['grid']
            
            # Cargar niveles de edificios
            self.building_levels = []
            for row in save_data['building_levels']:
                level_row = []
                for level_value in row:
                    level_row.append(BuildingLevel(level_value))
                self.building_levels.append(level_row)
            
            # Cargar historial
            self.history = save_data['history']
            self.events = save_data['events']
            
            # Recalcular estadísticas
            self.calculate_population()
            self.calculate_demand()
            
            self.add_message(f"📂 Ciudad cargada desde '{filename}'")
            return True
            
        except FileNotFoundError:
            self.add_message(f"❌ Archivo '{filename}' no encontrado")
            return False
        except Exception as e:
            self.add_message(f"❌ Error al cargar: {str(e)}")
            return False
    
    def run(self):
        """Ejecuta el bucle principal del juego"""
        while not self.game_over:
            self.display_city()
            choice = self.display_menu()
            
            if choice == "1":  # Construir
                self.handle_construction()
            elif choice == "2":  # Demoler
                self.handle_demolition()
            elif choice == "3":  # Estadísticas
                self.display_stats()
                input("\n⏎ Presiona Enter para continuar...")
            elif choice == "4":  # Impuestos
                self.set_tax_rate()
            elif choice == "5":  # Avanzar 1 mes
                self.calculate_monthly_updates()
                self.add_message("📅 Mes completado")
                time.sleep(1)
            elif choice == "6":  # Avanzar 1 año
                for _ in range(12):
                    self.calculate_monthly_updates()
                self.add_message("📅 Año completado")
                time.sleep(1)
            elif choice == "7":  # Guardar
                self.save_city()
            elif choice == "8":  # Cargar
                self.load_city()
            elif choice == "9":  # Logros
                self.show_achievements()
            elif choice == "0":  # Salir
                print("\n👋 ¡Gracias por jugar SimCity!")
                if input("¿Guardar antes de salir? (s/n): ").lower() == 's':
                    self.save_city()
                break
            else:
                self.add_message("❌ Opción no válida")
        
        if self.game_over:
            print("\n" + "="*60)
            print("🎮 ¡JUEGO TERMINADO!")
            print("="*60)
            print(f"\n🏙️  {self.city_name} - Año {self.year}")
            print(f"👥 Población final: {self.population:,}")
            print(f"💰 Presupuesto final: ${self.budget:,}")
            print(f"😊 Felicidad final: {self.happiness}%")
            
            # Mostrar causa del fin del juego
            print("\n📜 Causa:")
            for msg in self.message_log[-3:]:
                print(f"   {msg}")
            
            input("\n⏎ Presiona Enter para salir...")
    
    def handle_construction(self):
        """Maneja la interfaz de construcción"""
        build_choice = self.build_menu()
        
        zone_mapping = {
            "1": ZoneType.RESIDENTIAL,
            "2": ZoneType.COMMERCIAL,
            "3": ZoneType.INDUSTRIAL,
            "4": ZoneType.ROAD,
            "5": ZoneType.POWER_PLANT,
            "6": ZoneType.WATER_PLANT,
            "7": ZoneType.POLICE,
            "8": ZoneType.FIRE,
            "9": ZoneType.HOSPITAL,
            "10": ZoneType.SCHOOL,
            "11": ZoneType.PARK,
            "12": ZoneType.POWER_LINE
        }
        
        if build_choice in zone_mapping:
            zone_type = zone_mapping[build_choice]
            
            try:
                coords = input("Coordenadas (x y): ").strip().split()
                if len(coords) == 2:
                    x, y = int(coords[0]), int(coords[1])
                    self.build(zone_type, x, y)
                else:
                    self.add_message("❌ Formato inválido. Usa: x y")
            except ValueError:
                self.add_message("❌ Coordenadas inválidas")
        
        elif build_choice != "0":
            self.add_message("❌ Opción no válida")
    
    def handle_demolition(self):
        """Maneja la interfaz de demolición"""
        try:
            coords = input("Coordenadas para demoler (x y): ").strip().split()
            if len(coords) == 2:
                x, y = int(coords[0]), int(coords[1])
                self.demolish(x, y)
            else:
                self.add_message("❌ Formato inválido. Usa: x y")
        except ValueError:
            self.add_message("❌ Coordenadas inválidas")

# ===========================================
# FUNCIÓN PRINCIPAL
# ===========================================
def main():
    """Función principal del juego"""
    print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║    ███████╗██╗███╗   ███╗ ██████╗██╗████████╗██╗   ██╗      ║
║    ██╔════╝██║████╗ ████║██╔════╝██║╚══██╔══╝╚██╗ ██╔╝      ║
║    ███████╗██║██╔████╔██║██║     ██║   ██║    ╚████╔╝       ║
║    ╚════██║██║██║╚██╔╝██║██║     ██║   ██║     ╚██╔╝        ║
║    ███████║██║██║ ╚═╝ ██║╚██████╗██║   ██║      ██║         ║
║    ╚══════╝╚═╝╚═╝     ╚═╝ ╚═════╝╚═╝   ╚═╝      ╚═╝         ║
║                                                              ║
║                El Simulador de Ciudades Más Famoso           ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
    """)
    
    print("\n🎮 BIENVENIDO A SIMCITY")
    print("Construye y gestiona tu propia ciudad desde cero.")
    
    city_name = input("\n🏙️  ¿Cómo quieres llamar a tu ciudad? ").strip()
    if not city_name:
        city_name = "Nueva Ciudad"
    
    # Opciones de tamaño
    print("\n📏 Tamaño de la ciudad:")
    print("1. Pequeña (15x10)")
    print("2. Mediana (20x15)")
    print("3. Grande (25x20)")
    
    size_choice = input("Selecciona tamaño (1-3): ").strip()
    
    if size_choice == "1":
        width, height = 15, 10
    elif size_choice == "3":
        width, height = 25, 20
    else:
        width, height = 20, 15
    
    # Crear ciudad
    city = SimCity(city_name, width, height)
    
    # Mostrar tutorial breve
    print("\n" + "="*60)
    print("📚 TUTORIAL RÁPIDO:")
    print("="*60)
    print("1. Comienza construyendo zonas residenciales (🏠)")
    print("2. Añade zonas comerciales (🛒) e industriales (🏭)")
    print("3. Conecta todo con carreteras (🛣️)")
    print("4. Proporciona servicios: energía (⚡), agua (💧)")
    print("5. Añade policía (👮), bomberos (🚒), hospitales (🏥)")
    print("6. Controla impuestos (💰) y mantén felices a los ciudadanos (😊)")
    print("7. Avanza el tiempo (⏩) para ver crecer tu ciudad")
    print("="*60)
    input("\n⏎ Presiona Enter para comenzar...")
    
    # Ejecutar juego
    city.run()

if __name__ == "__main__":
    main()
