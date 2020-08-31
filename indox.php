<?php
define('mem_limit', return_bytes(ini_get('2000'))); //allowed memory

/*
SIMPLE TEST CLASS
*/
class test { }
$loop = 260;
$t = new Test();
for ($x=0;$x<=$loop;$x++) {
  $v = 'test'.$x;
  $t->$v = new Test();
  for ($y=0;$y<=$loop;$y++) {
    $v2 = 'test'.$y;
    $t->$v->$v2 = str_repeat('something to test! ', 200);
  }
}
/* ---------------- */


echo saferVarDumpObject($t);

function varDumpToString($v) {
  ob_start();
  var_dump($v);
  $content = ob_get_contents();
  ob_end_clean();
  return $content;
}

function saferVarDumpObject($var) {
  if (!is_object($var) && !is_array($var))
    return varDumpToString($var);

  $content = '';
  foreach($var as $v) {
    $content .= saferVarDumpObject($v);
  }
  //adding these smaller pieces to a single var works fine.
  //returning the complete larger piece gives memory error

  $length = strlen($content);
  $left = mem_limit-memory_get_usage(true);

  if ($left>$length)
    return $content; //enough memory left

  echo "WARNING! NOT ENOUGH MEMORY<hr>";
  if ($left>100) {
    return substr($content, 0, $left-100); //100 is a margin I choose, return everything you have that fits in the memory
  } else {
    return ""; //return nothing.
  }  
}

function return_bytes($val) {
    $val = trim($val);
    $last = strtolower($val[strlen($val)-1]);
    switch($last) {
        // The 'G' modifier is available since PHP 5.1.0
        case 'g':
            $val *= 1024;
        case 'm':
            $val *= 1024;
        case 'k':
            $val *= 1024;
    }

    return $val;
}
?>