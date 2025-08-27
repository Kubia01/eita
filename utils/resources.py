import os
import sys


def resource_path(relative_path: str) -> str:
	"""
	Resolve o caminho de um asset em tempo de execução, tanto quando o app
	está congelado via PyInstaller (onefile/onefolder) quanto em desenvolvimento.

	A estratégia tenta, na ordem:
	1) sys._MEIPASS (diretório de extração do PyInstaller em onefile)
	2) Diretório do executável (ao lado do binário)
	3) Raiz do projeto (um nível acima deste arquivo)
	4) Diretório de trabalho atual

	Retorna o primeiro caminho existente; caso nenhum exista, devolve um caminho
	construído a partir da melhor base disponível.
	"""
	base_candidates = []

	# 1) Onefile: diretório temporário de extração do PyInstaller
	if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
		base_candidates.append(sys._MEIPASS)  # type: ignore[attr-defined]

	# 2) Diretório do executável (útil para onefolder ou assets externos ao lado do binário)
	if getattr(sys, 'frozen', False) and hasattr(sys, 'executable'):
		base_candidates.append(os.path.dirname(os.path.abspath(sys.executable)))

	# 3) Em desenvolvimento: um nível acima deste arquivo tende a ser a raiz do projeto
	base_candidates.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

	# 4) Diretório de trabalho atual (fallback)
	base_candidates.append(os.getcwd())

	for base_dir in base_candidates:
		candidate = os.path.join(base_dir, relative_path)
		if os.path.exists(candidate):
			return candidate

	# Fallback: retorna um caminho montado a partir do primeiro candidato disponível
	return os.path.join(base_candidates[0], relative_path) if base_candidates else relative_path

