
from typing import List, Tuple, Dict
import json
import math


def calculate_panels(panel_width: int, panel_height: int, 
                    roof_width: int, roof_height: int) -> int:
    
    
    # Primero chequeo si el panel cabe en el techo al menos 1 vez probando el panel en ambos sentidos
    a = math.floor(roof_width/panel_width)
    b = math.floor(roof_width/panel_height)
    if a == 0 and b == 0:
        # si el panel no cabe a lo ancho en ninguno de los sentidos no cabe
        # print('no cabe')
        return 0

    c = math.floor(roof_height/panel_width)
    d = math.floor(roof_height/panel_height)
    if c == 0 and d == 0:
        # si el panel no cabe a lo largo en ninguno de los sentidos no cabe
        # print('no cabe')
        return 0

    

    # Calculo el area total del techo y de los paneles
    area_techo = roof_width*roof_height
    area_panel = panel_width*panel_height
    # Veo cuantas veces me cabe el panel en el area deseada
    n = math.floor( area_techo/area_panel )
    
    return n


def run_tests() -> None:
    with open('test_cases.json', 'r') as f:
        data = json.load(f)
        test_cases: List[Dict[str, int]] = [
            {
                "panel_w": test["panelW"],
                "panel_h": test["panelH"],
                "roof_w": test["roofW"],
                "roof_h": test["roofH"],
                "expected": test["expected"]
            }
            for test in data["testCases"]
        ]
    
    print("Corriendo tests:")
    print("-------------------")
    
    for i, test in enumerate(test_cases, 1):
        result = calculate_panels(
            test["panel_w"], test["panel_h"], 
            test["roof_w"], test["roof_h"]
        )
        passed = result == test["expected"]
        
        print(f"Test {i}:")
        print(f"  Panels: {test['panel_w']}x{test['panel_h']}, "
              f"Roof: {test['roof_w']}x{test['roof_h']}")
        print(f"  Expected: {test['expected']}, Got: {result}")
        print(f"  Status: {'✅ PASSED' if passed else '❌ FAILED'}\n")


def main() -> None:
    print("🐕 Wuuf wuuf wuuf 🐕")
    print("================================\n")
    
    run_tests()


if __name__ == "__main__":
    main()