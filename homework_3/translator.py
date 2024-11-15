import argparse
import toml

class Converter:
    def __init__(self, input_toml):
        self.input_toml = input_toml
        self.output_lines = []

    def parse_toml(self):
        try:
            data = toml.load(self.input_toml)
            self.convert(data)
        except toml.TomlDecodeError as e:
            raise ValueError(f"Ошибка синтаксиса в файле TOML: {e}")

    def convert(self, data):
        for key, value in data.items():
            self.output_lines.append(f"{key} := {self.format_value(value)}")

    def format_value(self, value):
        if isinstance(value, dict):
            return self.format_dict(value)
        elif isinstance(value, list):
            return "[" + ", ".join(map(str, value)) + "]"
        return str(value)

    def format_dict(self, value, indent_level=2):
        indent = ' ' * indent_level
        dict_lines = []
        for key, val in value.items():
            if isinstance(val, dict):
                dict_lines.append(f"{indent}{key} := {self.format_dict(val, indent_level + 2)}")
            else:
                dict_lines.append(f"{indent}{key} = {self.format_value(val)}")
        return "{\n" + "\n".join(dict_lines) + f"\n{indent[:-2]}}}"

    def get_output(self):
        return "\n".join(self.output_lines)

def main():
    parser = argparse.ArgumentParser(description="Конвертер TOML в учебный конфигурационный язык.")
    parser.add_argument('input_file', type=str, help='Путь к входному файлу TOML')
    parser.add_argument('output_file', type=str, help='Путь к выходному файлу')

    args = parser.parse_args()

    converter = Converter(args.input_file)

    try:
        converter.parse_toml()
        output = converter.get_output()

        with open(args.output_file, 'w') as f:
            f.write(output)

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
