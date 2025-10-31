# alu-scripting README

This repository, named alu-scripting, is a collection of Ruby scripts utilizing regular expressions. Each script focuses on different patterns using the `scan` method to extract specific text from the provided input.

### Regular Exp

The scripts are designed to showcase regular expressions in the context of pattern matching within text data.

### Usage

To run these scripts, ensure you have Ruby installed on your system. Execute each script by passing the desired text as a command-line argument.

#### Examples:

```ruby
#!/usr/bin/env ruby
# 0-simply_match_school.rb
puts ARGV[0].scan(/School/).join

#!/usr/bin/env ruby
# 1-repetition_token_0.rb
puts ARGV[0].scan(/hbt{2,5}n/).join

#!/usr/bin/env ruby
# 2-repetition_token_1.rb
puts ARGV[0].scan(/hb?tn/).join

#!/usr/bin/env ruby
# 3-repetition_token_2.rb
puts ARGV[0].scan(/hbt+n/).join

#!/usr/bin/env ruby
# 4-repetition_token_3.rb
puts ARGV[0].scan(/hbt*n/).join

#!/usr/bin/env ruby
# 5-beginning_and_end.rb
puts ARGV[0].scan(/^h.n$/).join

#!/usr/bin/env ruby
# 6-phone_number.rb
puts ARGV[0].scan(/^[0-9]{10}$/).join

