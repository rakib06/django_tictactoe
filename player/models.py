from django.db import models
from django.contrib.auth.models import User

class Invitation(models.Model):
    from_user = models.ForeignKey(User, related_name="invitation_sent")
    to_user = models.ForeignKey(User, related_name="invitations_received")
    message = models.CharField(max_length=300)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.from_user.username + ' to ' + self.to_user.username + ' '+str(self.timestamp)[:-13]