import asyncio
import time
from functools import wraps

# Decorator to log the execution time of a function
def log_execution_time(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        result = await func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

# Asynchronous function to simulate a network call
@log_execution_time
async def async_network_call(duration):
    print(f"Starting network call for {duration} seconds...")
    await asyncio.sleep(duration)
    print(f"Network call for {duration} seconds completed.")
    return f"Result from network call of {duration} seconds"

# Metaclass to add a class-level method dynamically
class Meta(type):
    def __new__(cls, name, bases, dct):
        dct['dynamic_method'] = cls.dynamic_method
        return super().__new__(cls, name, bases, dct)

    @staticmethod
    def dynamic_method():
        print("This is a dynamically added class-level method")

# Example class using the metaclass
class ExampleClass(metaclass=Meta):
    def __init__(self, value):
        self.value = value

    def display_value(self):
        print(f"Value: {self.value}")

# Main function to run asynchronous tasks
async def main():
    # Create an instance of ExampleClass
    example = ExampleClass(42)
    example.display_value()
    example.dynamic_method()

    # Run asynchronous network calls
    tasks = [async_network_call(i) for i in range(1, 4)]
    results = await asyncio.gather(*tasks)
    print("All network calls completed.")
    print("Results:", results)

# Entry point for the script
if __name__ == "__main__":
    asyncio.run(main())
