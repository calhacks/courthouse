# Forked from Gavel by HackMIT / Anish Athalye (me@anishathalye.com)
#
# This software and Gavel are both released under AGPLv3. 
# See the included LICENSE.txt for details.

if __name__ == '__main__':
    from courthouse.models import db
    db.create_all()
