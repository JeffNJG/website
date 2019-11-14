format 221

classcanvas 128002 class_ref 128002 // User
  classdiagramsettings member_max_width 0 end
  xyz 379 125 2000
end
classcanvas 128130 class_ref 128130 // Profile
  classdiagramsettings member_max_width 0 end
  xyz 665 7 2000
end
classcanvas 128258 class_ref 128258 // Project
  classdiagramsettings member_max_width 0 end
  xyz 212 73 2000
end
classcanvas 128386 class_ref 128386 // Event
  classdiagramsettings member_max_width 0 end
  xyz 653 259 2000
end
classcanvas 128514 class_ref 128514 // EventMedia
  classdiagramsettings member_max_width 0 end
  xyz 407 394 2000
end
classcanvas 129026 class_ref 128642 // Article
  classdiagramsettings member_max_width 0 end
  xyz 75 372 2000
end
classcanvas 129154 class_ref 128770 // ChildGroup
  classdiagramsettings member_max_width 0 end
  xyz 60 179 2000
end
classcanvas 129922 class_ref 128898 // Participation
  classdiagramsettings member_max_width 0 end
  xyz -1 47 2000
end
relationcanvas 128642 relation_ref 128002 // possede
  from ref 128002 z 2001 label "possede" italic max_width 255 xyz 533 126 2001 to ref 128130
  no_role_a no_role_b
  multiplicity_a_pos 647 115 3000 multiplicity_b_pos 457 176 3000
end
relationcanvas 128898 relation_ref 128258 // contient
  from ref 128514 z 2001 label "contient" italic max_width 255 xyz 547 360 2001 to ref 128386
  no_role_a no_role_b
  multiplicity_a_pos 635 339 3000 multiplicity_b_pos 495 417 3000
end
relationcanvas 130178 relation_ref 128514 // redige
  from ref 129026 z 2001 label "redige" italic max_width 255 xyz 245 364 2001 to point 396 349
  line 130306 z 2001 to ref 128002
  no_role_a no_role_b
  multiplicity_a_pos 390 244 3000 multiplicity_b_pos 135 411 3000
end
relationcanvas 130434 relation_ref 128642 // publie
  from ref 128002 z 2001 label "publie" italic max_width 255 xyz 533 237 2001 to ref 128386
  no_role_a no_role_b
  multiplicity_a_pos 637 316 3000 multiplicity_b_pos 457 210 3000
end
relationcanvas 130690 relation_ref 135298 // participe
  from ref 128258 z 2001 label "participe" italic max_width 255 xyz 308 132 3000 to ref 128002
  no_role_a no_role_b
  multiplicity_a_pos 363 177 3000 multiplicity_b_pos 292 138 3000
end
relationcanvas 130818 relation_ref 135426 // <association>
  decenter_begin 708
  decenter_end 181
  from ref 129154 z 2001 to point 114 39
  line 130946 z 2001 to ref 128130
  no_role_a no_role_b
  no_multiplicity_a no_multiplicity_b
end
line 131202 -_-_
  from ref 130818 z 2002 to ref 129922
end
