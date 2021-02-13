import sqlite3

conn = sqlite3.connect('Database.db')
c = conn.cursor()

def get_prefix(client, msg):
    serverId = str(msg.guild.id)
    c.execute("SELECT Prefix FROM ServerConfig WHERE ServerId = ?", (serverId,))
    prefix = c.fetchall()
    prefix = prefix[0][0]
    return prefix


def get_autorole(client, msg):
    serverId = str(msg.guild.id)
    c.execute("SELECT AutoRoleId FROM AutoRoleConfig WHERE ServerId = ?", (serverId,))
    autoRoleId = c.fetchall()
    autoRoleId = autoRoleId[0][0]
    return autoRoleId