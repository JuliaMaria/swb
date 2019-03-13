 # init tables
        positions = range(N)
        matrixFields = [[posX, posY] for posX in positions for posY in positions]
        shuffle(matrixFields)

        self.tables = [Dinning_table(x, y) for x, y in matrixFields]
