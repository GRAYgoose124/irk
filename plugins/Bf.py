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
import logging

from plugin import Plugin


logger = logging.getLogger(__name__)


class Bf(Plugin):
    def __init__(self, handler):
        super().__init__(handler)
        self.commands = {
            'bf': self.bf
        }

    def bf(self, *data):
        # TODO: Complete
        print(data)
        if data[2][0] == '#':
            destination = data[2]
        else:
            destination = data[1]

        try:
            code_string = data[0].split(" ")[1]
        except IndexError:
            self.send_message("Get it right if you're gonna try.", destination)

        try:
            input_string = data[0].split(" ", 2)[2]
        except IndexError:
            input_string = ""

        max_loops = 1024
        tape_size = 24
        tape = [0]*tape_size
        tape_pos = int(tape_size / 2)
        i_saved = []

        output_string = ""

        loop_n = 0
        i = 0
        while i < len(code_string):
            if code_string[i] == '+':
                tape[tape_pos] += 1
            elif code_string[i] == '-':
                tape[tape_pos] -= 1
            elif code_string[i] == '>':
                if tape_pos >= tape_size-1:
                    tape_pos = 0
                else:
                    tape_pos += 1
            elif code_string[i] == '<':
                if tape_pos == 0:
                    tape_pos = tape_size-1
                else:
                    tape_pos -= 1
            elif code_string[i] == ']':
                if tape[tape_pos] != 0 and loop_n < max_loops:
                    i = i_saved.pop()
                    loop_n += 1
                elif loop_n > max_loops:
                    loop_n = 0
            elif code_string[i] == '[':
                i_saved.append(i-1)
            elif code_string[i] == ',':
                if input_string != "":
                    tape[tape_pos] = ord(input_string[0])
                    input_string = input_string[1:]
                else:
                    break
            elif code_string[i] == '.':
                output_string += chr(tape[tape_pos])
            i += 1

        # TODO: Filter output string
        if output_string != "":
            message = "BF Output: " + output_string
        else:
            message = repr(tape)

        self.send_message(message, destination)
