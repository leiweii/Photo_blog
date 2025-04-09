import logging
import time
import json

logger = logging.getLogger('django.request')

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Début du traitement de la requête
        start_time = time.time()

        # Collecter les informations sur la requête
        request_info = {
            'method': request.method,
            'path': request.path,
            'user': str(request.user),
            'ip_address': self.get_client_ip(request),
        }

        # Log de début de requête
        logger.info(f"Début de requête: {json.dumps(request_info)}")

        # Traitement de la requête
        response = self.get_response(request)

        # Calcul du temps de traitement
        duration = time.time() - start_time

        # Collecter les informations de réponse
        response_info = {
            'status_code': response.status_code,
            'duration': f"{duration:.4f} secondes",
            **request_info
        }

        # Log de fin de requête
        if response.status_code >= 400:
            logger.error(f"Requête avec erreur: {json.dumps(response_info)}")
        else:
            logger.info(f"Fin de requête: {json.dumps(response_info)}")

        return response

    def get_client_ip(self, request):
        """
        Obtenir l'adresse IP du client
        """
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    
    
    
    