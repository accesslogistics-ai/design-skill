"""Verifica integridade do pacote sem depender de bibliotecas externas."""
import hashlib,json,sys
from pathlib import Path

BASE=Path(__file__).resolve().parents[1]
def verify(base=BASE):
    manifest=base/'assets/sha256.json'
    if not manifest.exists(): return ['Inventário de integridade ausente.']
    checks=json.loads(manifest.read_text(encoding='utf-8')); errors=[]
    for relative,expected in checks.items():
        path=(base/relative).resolve()
        if not path.is_relative_to(base.resolve()): errors.append('Caminho fora do pacote: '+relative);continue
        if not path.is_file(): errors.append('Arquivo ausente: '+relative)
        elif hashlib.sha256(path.read_bytes()).hexdigest()!=expected: errors.append('Arquivo alterado: '+relative)
    return errors
if __name__=='__main__':
    errors=verify()
    print(json.dumps({'ok':not errors,'errors':errors,'scope':'Integridade dos arquivos inventariados, não avaliação visual nem assinatura de autoria.'},ensure_ascii=False,indent=2))
    sys.exit(1 if errors else 0)
