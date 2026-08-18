def hanoi(n, source, helper, destination):

    if n == 1:
        print(f"Move Disk {n} from {source} to {destination}")
        return

    hanoi(n-1, source,destination,helper)
    print(f"Move Disk {n} from {source} to {destination} ")   

    hanoi(n-1, helper, source, destination)
    
hanoi(3,"A","B","C")