# АССЕМБЛЕР
import sys
import csv

def process_file(input_file, bin_file, log_file):
    binary_data = []
    log_data = []

    with open(input_file, 'r') as file:
        for line in file:
            parts = line.split()
            instruction = parts[0]
            if instruction == "load_const":
                binary_data.append(numbers_to_bytes(18, int(parts[1])))
                log_data.append([18, int(parts[1])])
            if instruction == "read_mem":
                binary_data.append(bytes([37]))
                log_data.append([37, 0])
            if instruction == "write_mem":
                binary_data.append(numbers_to_bytes(99, int(parts[1])))
                log_data.append([99, int(parts[1])])
            if instruction == "sqrt":
                binary_data.append(numbers_to_bytes(52, int(parts[1])))
                log_data.append([52, int(parts[1])])

    with open(bin_file, "wb") as f:
        for elem in binary_data:
            f.write(elem)

    with open(log_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["A", "B"])
        writer.writerows(log_data)


def numbers_to_bytes(num1, num2):
    """Converts two numbers into bytes (as before)."""
    if not (0 <= num1 <= 127 and 0 <= num2 <= 33554431):
        return None
    combined = (num1 << 25) | num2
    return combined.to_bytes(4, byteorder='big')

if __name__ == "__main__":
    input_file = sys.argv[1]
    bin_file = sys.argv[2]
    log_file = sys.argv[3]
    process_file(input_file, bin_file, log_file)
