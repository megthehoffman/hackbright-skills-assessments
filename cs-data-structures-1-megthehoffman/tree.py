"""Tree class and tree node class."""


class Node(object):
    """Node in a tree."""

    def __init__(self, data, children=None):
        children = children or []
        assert isinstance(children, list), \
            "children must be a list!"
        self.data = data
        self.children = children

    def __repr__(self):
        """Reader-friendly representation."""

        return "<Node {data}>".format(data=self.data)


class Tree(object):
    """Tree."""

    def __init__(self, root):
        self.root = root

    def __repr__(self):
        """Reader-friendly representation."""

        return "<Tree root={root}>".format(root=self.root)

    def get_nodes(self, data):
        """ Return a list of nodes with the given data

        For example::

            >>> b1 = Node("B")
            >>> b2 = Node("B")
            >>> e = Node("E")
            >>> c = Node("C", [ b1, e])
            >>> a = Node("A", [b2, c])
            >>> tree = Tree(a)
            >>> result = tree.get_nodes("B")
            >>> result == [b2, b1]
            True
            >>> tree.get_nodes("L")
            []

        """

        to_visit = [self.root]

        result = []

        while to_visit:
            current = to_visit.pop(0)
            # print(current)
            if current.data == data:
                result.append(current)

            to_visit.extend(current.children)

        # print(result)
        return result


if __name__ == "__main__":
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED. GOOD WORK!")
    print()