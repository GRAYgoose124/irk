#   Irk: irc bot
#   Copyright (C) 2016  Grayson Miller
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>

import irc

class IrcBot(IrcClient):
    def __init__():
        pass

    def _proc_privmsg(self, sender_nick, command, params):
        # SORT data into queries and channels
        # Put into dict/hash O(n) search...
        # TODO: Yield data to bot so the bot can asyncronously process it.
        # TODO: Offload to Bot class. Add more commands. (privileges,etc) (in plugins)
        if sender_nick == self.config['owner']:
            if command  ==  '!quit':
                self._quit()
            elif command == '!join':
                if params[0] == '#':
                    self.join(params[0])
            elif command == '!ping':
                if len(tokens) > 2:
                    self._privmsg_ping(tokens[2])
                else:
                    self._privmsg_ping(sender_nick)
