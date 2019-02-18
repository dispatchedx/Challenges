'''
I should have made variables equal to each string like closed = ''CLOSED"

'''
def traverse_TCP_states(events):
    state = "CLOSED"  # initial state, always
    for event in events:
        if state == 'CLOSED':
            if event == 'APP_PASSIVE_OPEN':
                state = 'LISTEN'
            elif event == 'APP_ACTIVE_OPEN':
                state = 'SYN_SENT'
            else:
                return 'ERROR'

        elif state == 'LISTEN':
            if event == 'RCV_SYN':
                state = 'SYN_RCVD'
            elif event == 'APP_SEND':
                state = 'SYN_SENT'
            elif event == 'APP_CLOSE':
                state = 'CLOSED'
            else:
                return 'ERROR'

        elif state == 'SYN_RCVD':
            if event == 'APP_CLOSE':
                state = 'FIN_WAIT_1'
            elif event == 'RCV_ACK':
                state = 'ESTABLISHED'
            else:
                return 'ERROR'

        elif state == 'SYN_SENT':
            if event == 'RCV_SYN':
                state = 'SYN_RCVD'
            elif event == 'RCV_SYN_ACK':
                state = 'ESTABLISHED'
            elif event == 'APP_CLOSE':
                state = 'CLOSED'
            else:
                return 'ERROR'

        elif state == 'ESTABLISHED':
            if event == 'APP_CLOSE':
                state = 'FIN_WAIT_1'
            elif event == 'RCV_FIN':
                state = 'CLOSE_WAIT'
            else:
                return 'ERROR'

        elif state == 'FIN_WAIT_1':
            if event == 'RCV_FIN':
                state = 'CLOSING'
            elif event == 'RCV_FIN_ACK':
                state = 'TIME_WAIT'
            elif event == 'RCV_ACK':
                state = 'FIN_WAIT_2'
            else:
                return 'ERROR'

        elif state == 'CLOSING':
            if event == 'RCV_ACK':
                state = 'TIME_WAIT'
            else:
                return 'ERROR'

        elif state == 'FIN_WAIT_2':
            if event == 'RCV_FIN':
                state = 'TIME_WAIT'
            else:
                return 'ERROR'

        elif state == 'TIME_WAIT':
            if event == 'APP_TIMEOUT':
                state = 'CLOSED'
            else:
                return 'ERROR'

        elif state == 'CLOSE_WAIT':
            if event == 'APP_CLOSE':
                state = 'LAST_ACK'
            else:
                return 'ERROR'

        elif state == 'LAST_ACK':
            if event == 'RCV_ACK':
                state = 'CLOSED'
            else:
                return 'ERROR'

    return state



print(traverse_TCP_states(["APP_ACTIVE_OPEN","RCV_SYN_ACK","RCV_FIN"]))# "CLOSE_WAIT")
print(traverse_TCP_states(["APP_PASSIVE_OPEN",  "RCV_SYN","RCV_ACK"]))# "ESTABLISHED")
print(traverse_TCP_states(["APP_ACTIVE_OPEN","RCV_SYN_ACK","RCV_FIN","APP_CLOSE"]))#, "LAST_ACK")
print(traverse_TCP_states(["APP_ACTIVE_OPEN"]))#, "SYN_SENT")
print(traverse_TCP_states(["APP_PASSIVE_OPEN","RCV_SYN","RCV_ACK","APP_CLOSE","APP_SEND"]))#, "ERROR")