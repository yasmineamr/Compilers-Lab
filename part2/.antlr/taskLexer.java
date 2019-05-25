// Generated from /Users/yasmineamr/Desktop/Semester 10/Compilers_lab/Compiler/part2/task.g4 by ANTLR 4.7
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class taskLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.7", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		NEWLINE=1, REG=2, MEMORY=3, IMMEDIATE=4, SPACE=5, SEPARATOR=6, COMMAND=7;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] ruleNames = {
		"NEWLINE", "REG", "MEMORY", "IMMEDIATE", "SPACE", "SEPARATOR", "COMMAND"
	};

	private static final String[] _LITERAL_NAMES = {
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, "NEWLINE", "REG", "MEMORY", "IMMEDIATE", "SPACE", "SEPARATOR", "COMMAND"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public taskLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "task.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\t@\b\1\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\3\2\6\2\23\n\2\r\2\16\2"+
		"\24\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\6\5\37\n\5\r\5\16\5 \3\5\7\5$\n\5"+
		"\f\5\16\5\'\13\5\3\5\6\5*\n\5\r\5\16\5+\3\5\5\5/\n\5\3\6\3\6\3\7\3\7\3"+
		"\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b?\n\b\2\2\t\3\3\5\4\7\5\t\6"+
		"\13\7\r\b\17\t\3\2\b\4\2\f\f\17\17\3\2CF\3\2\63;\3\2\62;\3\2\62\63\4\2"+
		"\13\13\"\"\2F\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2"+
		"\2\2\2\r\3\2\2\2\2\17\3\2\2\2\3\22\3\2\2\2\5\26\3\2\2\2\7\31\3\2\2\2\t"+
		".\3\2\2\2\13\60\3\2\2\2\r\62\3\2\2\2\17>\3\2\2\2\21\23\t\2\2\2\22\21\3"+
		"\2\2\2\23\24\3\2\2\2\24\22\3\2\2\2\24\25\3\2\2\2\25\4\3\2\2\2\26\27\t"+
		"\3\2\2\27\30\7Z\2\2\30\6\3\2\2\2\31\32\7]\2\2\32\33\5\5\3\2\33\34\7_\2"+
		"\2\34\b\3\2\2\2\35\37\t\4\2\2\36\35\3\2\2\2\37 \3\2\2\2 \36\3\2\2\2 !"+
		"\3\2\2\2!%\3\2\2\2\"$\t\5\2\2#\"\3\2\2\2$\'\3\2\2\2%#\3\2\2\2%&\3\2\2"+
		"\2&/\3\2\2\2\'%\3\2\2\2(*\t\6\2\2)(\3\2\2\2*+\3\2\2\2+)\3\2\2\2+,\3\2"+
		"\2\2,-\3\2\2\2-/\7d\2\2.\36\3\2\2\2.)\3\2\2\2/\n\3\2\2\2\60\61\t\7\2\2"+
		"\61\f\3\2\2\2\62\63\7.\2\2\63\64\5\13\6\2\64\16\3\2\2\2\65\66\7C\2\2\66"+
		"\67\7C\2\2\67?\7C\2\289\7C\2\29:\7F\2\2:?\7F\2\2;<\7K\2\2<=\7P\2\2=?\7"+
		"E\2\2>\65\3\2\2\2>8\3\2\2\2>;\3\2\2\2?\20\3\2\2\2\t\2\24 %+.>\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}