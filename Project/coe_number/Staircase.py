def display_staircase(base: int, display: str) -> str:
    data = []
    for i in range(1, base + 1):
        data.append(f"{display*i:>{base}}") # :> shift ไปทางขวามือ
    
    return "\n".join(data)
