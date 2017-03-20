import pyparsing as pp
comment_blk = pp.Regex("COMMENT[\s\S]*?ENDCOMMENT")
comment_eol = pp.Regex(":.*") 
comments = pp.Combine(comment_blk | comment_eol)

