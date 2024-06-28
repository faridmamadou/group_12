from typing import List, Union, Tuple

class Array:
    
    "__init__(self, data): Initialise le tableau avec la liste `data`."
    def __init__(self, data: Union[List[int], List[List[int]]]) -> None:
       
        if isinstance(data, list):
            if all(isinstance(d, list) for d in data):  # Tableau 2D
                self.data = data
                self.shape = (len(data), len(data[0]))
            else:  # Tableau 1D
                self.data = [data]
                self.shape = (1, len(data))
        else:
            raise TypeError("`data` doit être une liste.")

    def __repr__(self) -> str:
        return f"Array({self.data})"
    
    "__len__(self): Renvoie la longueur du tableau (nombre d'éléments en 1D, nombre de lignes en 2D)."
    def __len__(self) -> int:
        return self.shape[1] if self.shape[0] == 1 else self.shape[0]
    
    
    "shape: Propriété qui renvoie la forme du tableau (lignes, colonnes)."
    @property
    def shape(self) -> Tuple[int, int]:
        return self._shape

    @shape.setter
    def shape(self, value: Tuple[int, int]) -> None:
        self._shape = value



    "__getitem__(self, key): Accède aux éléments du tableau par indexation ou slicing."    
    def __getitem__(self, key: Union[int, Tuple[int, int], slice]) -> Union[int, float, 'Array']:
        
        if isinstance(key, tuple):
            row, col = key
            return self.data[row][col]
        elif isinstance(key, slice):
            start = key.start or 0
            stop = key.stop or self.shape[1]
            step = key.step or 1

            if self.shape[0] == 1:  # Tableau 1D
                return Array(self.data[0][start:stop:step])
            else:  # Tableau 2D
                return Array([row[start:stop:step] for row in self.data])
        elif isinstance(key, int):
            if self.shape[0] == 1:
                return self.data[0][key]
            else:
                return Array(self.data[key])
        else:
            raise TypeError("Indexation invalide.")
        

    "__setitem__(self, key, value): Modifie les éléments du tableau par indexation."    
    def __setitem__(self, key: Union[int, Tuple[int, int]], value: Union[int, float]) -> None:
        
        if isinstance(key, tuple):
            row, col = key
            self.data[row][col] = value
        elif isinstance(key, int):
            if self.shape[0] == 1:
                self.data[0][key] = value
            else:
                self.data[key] = value
        else:
            raise TypeError("Indexation invalide.")

    def _elementwise_operation(self, other: Union['Array', int, float], op) -> 'Array':
        
        if isinstance(other, Array):
            if self.shape != other.shape:
                raise ValueError("Les tableaux doivent avoir la même forme pour l'opération.")
            result = [[op(x, y) for x, y in zip(row_self, row_other)] for row_self, row_other in zip(self.data, other.data)]
        else:
            result = [[op(x, other) for x in row] for row in self.data]
        return Array(result if self.shape[0] > 1 else result[0])
    

   
    " _add__(self, other): Additionne deux tableaux élément par élément."
    def __add__(self, other: Union['Array', int, float]) -> 'Array':
        return self._elementwise_operation(other, lambda x, y: x + y)
    
    
    "_sub__(self, other): Soustrait deux tableaux élément par élément."
    def __sub__(self, other: Union['Array', int, float]) -> 'Array':
        return self._elementwise_operation(other, lambda x, y: x - y)
    
    
    "__mul__(self, other): Multiplie deux tableaux élément par élément."
    def __mul__(self, other: Union['Array', int, float]) -> 'Array':
        return self._elementwise_operation(other, lambda x, y: x * y)
    

    " __truediv__(self, other): Divise deux tableaux élément par élément."
    def __truediv__(self, other: Union['Array', int, float]) -> 'Array':
        return self._elementwise_operation(other, lambda x, y: x / y)
    

    "    __matmul__(self, other): Produit scalaire de deux tableaux 1D."
    def __matmul__(self, other: 'Array') -> Union[int, float]:
      
        if self.shape[0] != 1 or other.shape[0] != 1:
            raise ValueError("Le produit scalaire est uniquement supporté pour les tableaux 1D.")
        if self.shape[1] != other.shape[1]:
            raise ValueError("Les tableaux doivent avoir la même longueur pour le produit scalaire.")
        return sum(x * y for x, y in zip(self.data[0], other.data[0]))
    


    " __contains__(self, item): Recherche un élément dans le tableau."
    def __contains__(self, item: Union[int, float]) -> bool:
        return any(item in row for row in self.data)

if __name__ == "__main__":
    # Quelques tests pour vérifier les fonctionnalités
    a = Array([1, 2, 3])
    b = Array([4, 5, 6])
    c = Array([[1, 2], [3, 4]])
    d = Array([[5, 6], [7, 8]])

    print("Array a:", a)
    print("Array b:", b)
    print("Array c:", c)
    print("Array d:", d)

    # Affichage taille des tableaux
    print("Taille des tableaux:")
    print("a:",len(a))
    print("b:",len(d))

    # Affichage de la dimension
    print("Dimensions des tableaux")
    print("a:",a.shape)
    print("d:",d.shape)
    
    # Operations élément par élément
    print("a + b:", a + b)
    print("a - b:", a - b)
    print("a * 2:", a * 2)
    print("c + d:", c + d)
    print("a*b:", a * b)
    
    # Produit scalaire
    print("a @ b:", a @ b)
    
    # Contient un élément
    print("5 in a:", 5 in a)
    
    # Indexation et slicing
    print("a[1]:", a[1])
    print("c[1, 1]:", c[1, 1])
    print("a[0:2]:", a[0:2])
    print("c[:, 1]:", c[:, 1])
