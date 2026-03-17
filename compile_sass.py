"""
Módulo de automação para compilação de folhas de estilo Sass.
"""

import sass
import os
import sys

def run_compilation():
    """
    Localiza scss em src/static/scss e gera css em src/static/css.
    """
    base_path = os.getcwd()
    scss_dir = os.path.join(base_path, "src", "static", "scss")
    css_dir = os.path.join(base_path, "src", "static", "css")

    if not os.path.exists(scss_dir):
        print(f"Erro: Diretorio de origem nao encontrado: {scss_dir}")
        sys.exit(1)

    if not os.path.exists(css_dir):
        os.makedirs(css_dir)

    try:
        # A funcao compile gera os arquivos .css correspondentes aos .scss
        # que nao iniciam com underscore (_) no nome.
        sass.compile(dirname=(scss_dir, css_dir), output_style="compressed")
        print(f"Compilacao concluida. Destino: {css_dir}")
    except sass.CompileError as e:
        print(f"Erro de sintaxe no Sass:\n{e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    run_compilation()