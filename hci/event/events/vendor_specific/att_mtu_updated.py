from struct import unpack_from

from .. import VendorSpecificEvent


class ATT_MtuUpdated(VendorSpecificEvent):
    @property
    def conn_handle(self):
        OFFSET, SIZE_OCTETS = 6, 2
        conn_handle = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<H', conn_handle)[0]

    @property
    def pdu_length(self):
        OFFSET, SIZE_OCTETS = 8, 1
        pdu_length = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<B', pdu_length)[0]

    @property
    def mtu(self):
        OFFSET, SIZE_OCTETS = 9, 2
        mtu = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<H', mtu)[0]

    def __str__(self):
        return super().__str__() + '\n' + '\n'.join([
            'Connection Handle: {} ({})',
            'PDU Length: {} ({})',
            'MTU: {} ({})']).format(
            hex(self.conn_handle),
            int(self.conn_handle),
            hex(self.pdu_length),
            int(self.pdu_length),
            hex(self.mtu),
            int(self.mtu))
