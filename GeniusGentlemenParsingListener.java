// Generated from GeniusGentlemenParsing.g4 by ANTLR 4.7.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link GeniusGentlemenParsingParser}.
 */
public interface GeniusGentlemenParsingListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link GeniusGentlemenParsingParser#start}.
	 * @param ctx the parse tree
	 */
	void enterStart(GeniusGentlemenParsingParser.StartContext ctx);
	/**
	 * Exit a parse tree produced by {@link GeniusGentlemenParsingParser#start}.
	 * @param ctx the parse tree
	 */
	void exitStart(GeniusGentlemenParsingParser.StartContext ctx);
	/**
	 * Enter a parse tree produced by {@link GeniusGentlemenParsingParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(GeniusGentlemenParsingParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link GeniusGentlemenParsingParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(GeniusGentlemenParsingParser.ExprContext ctx);
}