from deta import Deta

deta = Deta()

# Our url database
links_db = deta.Base("links")

# Our snapshots database
snapshots_db = deta.Base("snapshots")

# Our QR Code storage drive
qr_drive = deta.Drive("codes")