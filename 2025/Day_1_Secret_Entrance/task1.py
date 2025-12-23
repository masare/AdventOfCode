
ROTATIONS_TXT: str = "input.txt"

class Node:
    def __init__(self, value: int) -> None:

        self.value: int = value
        self.next: Node | None = None
        self.prev: Node | None = None    

    # def left(self, distance: int) -> Node:
    #     if distance == 0:
    #         return
    #     return 
    #     self.value -= distance
    #     while self.value < 0:
    #         self.value += 100
    
    # def right(self, distance: int) -> None:
    #     self.value += distance
    #     while self.value > 99:
    #         self.value -= 100

def rotate(current_node: Node, direction: str, distance: int) -> Node:
    if distance == 0:
        return current_node
    
    if direction == 'L':
        # return rotate(current_node.prev, direction, distance-1)    
        for _ in range(distance):
            current_node = current_node.prev
            # print(f'Prev: {current_node.value}')
    elif direction == 'R':
        # return rotate(current_node.next, direction, distance-1)
        for _ in range(distance):
            current_node = current_node.next
            # print(f'Next: {current_node.value}')
    else:
        pass
    
    return current_node

def nodes_maker():
    nodes: list[Node] = []
    for i in range(100):
        node: Node = Node(i)
        nodes.append(node)

    for ind, node in enumerate(nodes):
        node.prev = nodes[ind-1]
        if ind == 99:
            node.next = nodes[0]
        else:
            node.next = nodes[ind+1]

    return nodes

def main() -> None:
    nodes: list[Node] = nodes_maker()
    dial: None | Node = None
    password: int = 0
    with open(ROTATIONS_TXT, 'r') as f:
        dial = nodes[50]
        print(f'The dial starts by pointing at {dial.value}')
        
        for ind, step in enumerate(f.readlines()):
            dial = rotate(dial, direction=step[0], distance=int(step[1:]))
            print(f'The dial is rotated {step} to point at {dial.value}')
            if dial.value == 0:
                password += 1

    print(f'\n\n\nThe password is {password}')


if __name__ == "__main__":
    main()