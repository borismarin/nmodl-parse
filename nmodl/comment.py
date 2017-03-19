import pyparsing as pp
comment_blk = pp.Regex("COMMENT[\s\S]*?ENDCOMMENT")

