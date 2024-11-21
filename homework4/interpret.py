# ИНТЕРПРЕТАТОР
import sys
import csv
import math

def interpret(bin_file, output_file, start_mem, end_mem):
    memory = [0] * 1024
    battery_register = 0
    instr = decode_file(bin_file)
    i = 0
    while i < len(instr):
        if instr[i] == 18:
            battery_register = instr[i+1]
            i += 2
        if instr[i] == 37:
            print(battery_register)
            i += 1
        if instr[i] == 99:
            if instr[i+1] >= start_mem and instr[i+1] <= end_mem:
                memory[instr[i+1]] = battery_register
            else:
                print("Недопустимое значение для ячейки памяти")
            i += 2
        if instr[i] == 52:
            if start_mem + instr[i+1] <= end_mem:
                memory[start_mem + instr[i+1]] **= 0.5
            else:
                print("Недопустимое значение для ячейки памяти")
            i += 2

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        fieldnames = ["BR"] + [str(i) for i in range(1024)]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        data_dict = {"BR": battery_register}
        data_dict.update({str(i): value for i, value in enumerate(memory)})
        writer.writerow(data_dict)
    


def bytes_to_numbers(byte_data):
    if len(byte_data) == 1:
        return int.from_bytes(byte_data, byteorder='big')

    if len(byte_data) == 4:
        combined = int.from_bytes(byte_data, byteorder='big')
        num1 = (combined >> 25) & 0x7F
        num2 = combined & 0x1FFFFFF
        return num1, num2
    else:
        return None  # Handle invalid byte lengths


def decode_file(filename):
    numbers = []
    try:
        with open(filename, 'rb') as f:
            while True:
                chunk = f.read(1) # Try to read 4 bytes first
                if not chunk:
                    break
                decoded = bytes_to_numbers(chunk)
                if decoded == 37:
                    numbers.append(decoded)
                else:
                    chunk2 = f.read(3);
                    decoded = bytes_to_numbers(chunk + chunk2)
                    numbers.extend(decoded)
                if decoded is None:
                    break # end of file
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    return numbers

if __name__ == "__main__":
    bin_file = sys.argv[1]
    output_file = sys.argv[2]
    start_mem = int(sys.argv[3])
    end_mem = int(sys.argv[4])
    interpret(bin_file, output_file, start_mem, end_mem)
