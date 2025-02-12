

class PdoReadError(Exception):
    
    def __init__(self, failed_pdo_ids: list[int]):
        if not failed_pdo_ids:
            raise ValueError('PdoReadError expects at least one Id of a PDO for which the read failed.')
        self.failed_pdo_ids = failed_pdo_ids

    def __str__(self):
        if not self.failed_pdo_ids:
            return ''
        else:
            text = 'PDO{}'.format(self.failed_pdo_ids[0])
            for i in range(1, len(self.failed_pdo_ids)):
                text += ',PDO{}'.format(self.failed_pdo_ids[i])
            return text

