import json
import os
from typing import List, Dict, Any, Optional

class QuoteStorage:
    """Gestionnaire de stockage des citations inspirantes."""
    
    def __init__(self, filepath: str = "quotes.json"):
        """
        Initialise le gestionnaire de stockage.
        
        Args:
            filepath: Chemin vers le fichier JSON de stockage.
        """
        self.filepath = filepath
        self._ensure_storage_exists()
    
    def _ensure_storage_exists(self) -> None:
        """Crée le fichier de stockage s'il n'existe pas."""
        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w', encoding='utf-8') as f:
                json.dump([], f)
    
    def load_quotes(self) -> List[Dict[str, Any]]:
        """
        Charge toutes les citations depuis le fichier de stockage.
        
        Returns:
            Liste de dictionnaires représentant les citations.
        """
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    
    def save_quotes(self, quotes: List[Dict[str, Any]]) -> None:
        """
        Sauvegarde toutes les citations dans le fichier de stockage.
        
        Args:
            quotes: Liste de dictionnaires représentant les citations.
        """
        with open(self.filepath, 'w', encoding='utf-8') as f:
            json.dump(quotes, f, indent=2, ensure_ascii=False)
    
    def add_quote(self, text: str, author: str, category: Optional[str] = None) -> Dict[str, Any]:
        """
        Ajoute une nouvelle citation au stockage.
        
        Args:
            text: Texte de la citation.
            author: Auteur de la citation.
            category: Catégorie optionnelle de la citation.
            
        Returns:
            La citation ajoutée sous forme de dictionnaire.
        """
        quotes = self.load_quotes()
        
        new_id = max([quote.get('id', 0) for quote in quotes], default=0) + 1
        
        new_quote = {
            'id': new_id,
            'text': text,
            'author': author,
            'category': category
        }
        
        quotes.append(new_quote)
        self.save_quotes(quotes)
        
        return new_quote
    
    def remove_quote(self, quote_id: int) -> bool:
        """
        Supprime une citation par son ID.
        
        Args:
            quote_id: ID de la citation à supprimer.
            
        Returns:
            True si la citation a été supprimée, False sinon.
        """
        quotes = self.load_quotes()
        initial_length = len(quotes)
        quotes = [quote for quote in quotes if quote.get('id') != quote_id]
        if len(quotes) < initial_length:
            self.save_quotes(quotes)
            return True
        return False

# Fonctions globales pour compatibilité avec le CLI
def load_quotes(filepath: str = "quotes.json") -> List[Dict[str, Any]]:
    """Charge les citations depuis un fichier."""
    storage = QuoteStorage(filepath)
    return storage.load_quotes()

def save_quotes(quotes: List[Dict[str, Any]], filepath: str = "quotes.json") -> None:
    """Sauvegarde les citations dans un fichier."""
    storage = QuoteStorage(filepath)
    storage.save_quotes(quotes)

def load_quotes_from_file(filepath: str) -> List[Dict[str, Any]]:
    """Charge les citations depuis un fichier spécifique."""
    return load_quotes(filepath)

def save_quotes_to_file(quotes: List[Dict[str, Any]], filepath: str) -> None:
    """Sauvegarde les citations dans un fichier spécifique."""
    save_quotes(quotes, filepath)

def export_quotes_to_json(quotes: List[Dict[str, Any]], filepath: str) -> None:
    """Exporte les citations vers un fichier JSON."""
    save_quotes_to_file(quotes, filepath)

def import_quotes_from_json(filepath: str) -> List[Dict[str, Any]]:
    """Importe les citations depuis un fichier JSON."""
    return load_quotes_from_file(filepath)
