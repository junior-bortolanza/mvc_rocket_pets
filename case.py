class AlgumaCoisa:
    def __enter__(self):
        print("Estou entrando")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Esyou Saindo")

with AlgumaCoisa() as something:
    print("Estou no meio")
