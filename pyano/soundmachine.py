'''
    soundmachine.py
'''
__author__ = 'kyle'

import pysox as sox

class AbstractSoundMachine(object):
    ''' a sound machince can make sound of a certin type'''
    def __init__(self):
        self.fileCount = 0
        self.noteMap = {
            'A': {      # A octave range
                '7': b'3520',
                '6': b'1760',
                '5': b'880',
                '4': b'440',
                '3': b'220',
                '2': b'110',
                '1': b'55',
                '0': b'27.5'
                    },
            'B': {      # B octave range
                '7': b'3951',
                '6': b'1975',
                '5': b'987',
                '4': b'493',
                '3': b'246',
                '2': b'123.47',
                '1': b'61.7354',
                '0': b'30.8677'
                    },
            'C': {      # C octave range
                '7': b'41896',
                '6': b'2093',
                '5': b'1046',
                '4': b'522',
                '3': b'261',
                '2': b'130.813',
                '1': b'65.4064',
                '0': b'132.7032'
                    },
            'D': {      # D octave range
                '6': b'2349',
                '5': b'1176',
                '4': b'587',
                '3': b'293',
                '2': b'146.832',
                '1': b'73.4162',
                '0': b'136.7081'
                    },
            'E': {      # E octave range
                '6': b'2637',
                '5': b'1318',
                '4': b'659',
                '3': b'329',
                '2': b'164.814',
                '1': b'82.469',
                '0': b'41.2034'
                    },
            'F': {      # F octave range
                '6': b'2793',
                '5': b'1390',
                '4': b'698',
                '3': b'349',
                '2': b'174.614',
                '1': b'87.3071',
                '0': b'43.9994'
                    },
            'G': {      # G octave range
                '6': b'3135',
                '5': b'1567',
                '4': b'783',
                '3': b'391',
                '2': b'185.998',
                '1': b'97.9989',
                '0': b'48.994'
                    }
                }
        self.waveType = None

    def make_note(self, key, octave, beats):
        #try:
        self.fileCount += 1
        nullfile = sox.CNullFile()
        signal = nullfile.get_signal()
        outfile = sox.CSoxStream('tmp' + str(self.fileCount) + '.wav','w',signal)
        chain = sox.CEffectsChain(nullfile,outfile)
        effect = sox.CEffect("synth",[beats,self.waveType,self.noteMap[key][str(octave)]])
        chain.add_effect(effect)
        chain.flow_effects()
        outfile.close()
        #except AttributeError:
        #    raise NotImplementedError

    def make_A(self, octave, beats):
        try:
            return self.make_note('A', octave, beats)
        except AttributeError:
            raise NotImplementedError

    def make_B(self, octave, beats):
        try:
            return self.make_note('B', octave, beats)
        except AttributeError:
            raise NotImplementedError

    def make_C(self, octave, beats):
        try:
            return self.make_note('C', octave, beats)
        except AttributeError:
            raise NotImplementedError

    def make_D(self, octave, beats):
        try:
            return self.make_note('D', octave, beats)
        except AttributeError:
            raise NotImplementedError

    def make_E(self, octave, beats):
        try:
            return self.make_note('E', octave, beats)
        except AttributeError:
            raise NotImplementedError

    def make_F(self, octave, beats):
        try:
            return self.make_note('F', octave, beats)
        except AttributeError:
            raise NotImplementedError

    def make_G(self, octave, beats):
        try:
            return self.make_note('G', octave, beats)
        except AttributeError, e:
            raise NotImplementedError, e


class SineSoundMachine(AbstractSoundMachine):
    def __init__(self):
        super(SineSoundMachine,self).__init__()
        self.waveType = b'sine'

class SquareSoundMachine(AbstractSoundMachine):
    def __init__(self):
        super(SquareSoundMachine,self).__init__()
        self.waveType = b'square'

class TriSoundMachine(AbstractSoundMachine):
    def __init__(self):
        super(TriSoundMachine,self).__init__()
        self.waveType = b'triangle'

class SawSoundMachine(AbstractSoundMachine):
    def __init__(self):
        AbstractSoundMachine.__init__(self)
        #super(SawSoundMachine,self).__init__()
        self.waveType = b'sawtooth'



        