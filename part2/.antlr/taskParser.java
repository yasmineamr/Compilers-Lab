// Generated from /Users/yasmineamr/Desktop/Semester 10/Compilers_lab/Compiler/part2/task.g4 by ANTLR 4.7
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class taskParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		NEWLINE=1, REG=2, MEMORY=3, IMMEDIATE=4, SPACE=5, SEPARATOR=6, COMMAND=7;
	public static final int
		RULE_expr = 0, RULE_start = 1;
	public static final String[] ruleNames = {
		"expr", "start"
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

	@Override
	public String getGrammarFileName() { return "task.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public taskParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class ExprContext extends ParserRuleContext {
		public TerminalNode COMMAND() { return getToken(taskParser.COMMAND, 0); }
		public TerminalNode NEWLINE() { return getToken(taskParser.NEWLINE, 0); }
		public TerminalNode SPACE() { return getToken(taskParser.SPACE, 0); }
		public List<TerminalNode> REG() { return getTokens(taskParser.REG); }
		public TerminalNode REG(int i) {
			return getToken(taskParser.REG, i);
		}
		public TerminalNode SEPARATOR() { return getToken(taskParser.SEPARATOR, 0); }
		public TerminalNode MEMORY() { return getToken(taskParser.MEMORY, 0); }
		public TerminalNode IMMEDIATE() { return getToken(taskParser.IMMEDIATE, 0); }
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		ExprContext _localctx = new ExprContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_expr);
		try {
			setState(44);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(4);
				match(COMMAND);
				setState(5);
				match(NEWLINE);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(6);
				match(COMMAND);
				setState(7);
				match(SPACE);
				setState(8);
				match(REG);
				setState(9);
				match(SEPARATOR);
				setState(10);
				match(MEMORY);
				setState(11);
				match(NEWLINE);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(12);
				match(COMMAND);
				setState(13);
				match(SPACE);
				setState(14);
				match(MEMORY);
				setState(15);
				match(SEPARATOR);
				setState(16);
				match(REG);
				setState(17);
				match(NEWLINE);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(18);
				match(COMMAND);
				setState(19);
				match(SPACE);
				setState(20);
				match(REG);
				setState(21);
				match(SEPARATOR);
				setState(22);
				match(REG);
				setState(23);
				match(NEWLINE);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(24);
				match(COMMAND);
				setState(25);
				match(SPACE);
				setState(26);
				match(MEMORY);
				setState(27);
				match(SEPARATOR);
				setState(28);
				match(IMMEDIATE);
				setState(29);
				match(NEWLINE);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(30);
				match(COMMAND);
				setState(31);
				match(SPACE);
				setState(32);
				match(IMMEDIATE);
				setState(33);
				match(SEPARATOR);
				setState(34);
				match(MEMORY);
				setState(35);
				match(NEWLINE);
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(36);
				match(COMMAND);
				setState(37);
				match(SPACE);
				setState(38);
				match(REG);
				setState(39);
				match(NEWLINE);
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(40);
				match(COMMAND);
				setState(41);
				match(SPACE);
				setState(42);
				match(MEMORY);
				setState(43);
				match(NEWLINE);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StartContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public StartContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_start; }
	}

	public final StartContext start() throws RecognitionException {
		StartContext _localctx = new StartContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_start);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(49);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMAND) {
				{
				{
				setState(46);
				expr();
				}
				}
				setState(51);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\t\67\4\2\t\2\4\3"+
		"\t\3\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3"+
		"\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2"+
		"\3\2\3\2\3\2\3\2\3\2\3\2\5\2/\n\2\3\3\7\3\62\n\3\f\3\16\3\65\13\3\3\3"+
		"\2\2\4\2\4\2\2\2<\2.\3\2\2\2\4\63\3\2\2\2\6\7\7\t\2\2\7/\7\3\2\2\b\t\7"+
		"\t\2\2\t\n\7\7\2\2\n\13\7\4\2\2\13\f\7\b\2\2\f\r\7\5\2\2\r/\7\3\2\2\16"+
		"\17\7\t\2\2\17\20\7\7\2\2\20\21\7\5\2\2\21\22\7\b\2\2\22\23\7\4\2\2\23"+
		"/\7\3\2\2\24\25\7\t\2\2\25\26\7\7\2\2\26\27\7\4\2\2\27\30\7\b\2\2\30\31"+
		"\7\4\2\2\31/\7\3\2\2\32\33\7\t\2\2\33\34\7\7\2\2\34\35\7\5\2\2\35\36\7"+
		"\b\2\2\36\37\7\6\2\2\37/\7\3\2\2 !\7\t\2\2!\"\7\7\2\2\"#\7\6\2\2#$\7\b"+
		"\2\2$%\7\5\2\2%/\7\3\2\2&\'\7\t\2\2\'(\7\7\2\2()\7\4\2\2)/\7\3\2\2*+\7"+
		"\t\2\2+,\7\7\2\2,-\7\5\2\2-/\7\3\2\2.\6\3\2\2\2.\b\3\2\2\2.\16\3\2\2\2"+
		".\24\3\2\2\2.\32\3\2\2\2. \3\2\2\2.&\3\2\2\2.*\3\2\2\2/\3\3\2\2\2\60\62"+
		"\5\2\2\2\61\60\3\2\2\2\62\65\3\2\2\2\63\61\3\2\2\2\63\64\3\2\2\2\64\5"+
		"\3\2\2\2\65\63\3\2\2\2\4.\63";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}